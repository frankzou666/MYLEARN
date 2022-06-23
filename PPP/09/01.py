"""
Author:
Purpose:
Date：
"""

import argparse
from urllib.parse import  urlparse
import socket
from concurrent.futures import ThreadPoolExecutor,as_completed
import threading
import ipinfo
import mpl_toolkits
from mpl_toolkits.basemap import Basemap
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask,Response
import io
import datetime

app = Flask(__name__)


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def getDomains(file):
    """

    :param file:
    :return:
    """
    domains = set()
    with open(file,'r') as f:
        for line in f.readlines():
            url_host = urlparse(line).netloc
            url_host = url_host.split(':')[0]
            # remove \n
            domains.add(url_host.rstrip('\n'))

    return  domains



def getIPDetail(handler,ip):
    """

    :param handler:
    :param ip:
    :return:
    """
    try:
        ip_detail = handler.getDetails(ip)
        return ip_detail.all
    except Exception as e:
        print(e.__str__())




def getMap():
    """the entrance of this file"""
    file = 'history_data. txt'
    ip_access_token= 'efad093cc079bb'
    domains = getDomains(file)
    ips = set()
    handler = ipinfo.getHandler(ip_access_token)
    for domain in domains:
        try:
            ip = socket.gethostbyname(domain)
            ips.add(ip)
        except Exception as e:
            print(domain+e.__str__())
    complete_details = []

    with ThreadPoolExecutor(max_workers=10) as pool:
        complete_details_temp = []
        for ip in ips:
            complete_details_temp.append(pool.submit(getIPDetail, handler, ip))
    for item in complete_details_temp:
        complete_details.append(item.result())

    lat = []
    lon = []
    for item in complete_details:
        print(item['city'])
        lat.append(float(item['latitude']))
        lon.append(float(item['longitude']))
    print(lat)
    print(lon)
    fig, ax = plt.subplots(figsize=(40, 20))
    map = Basemap()
    # dark grey land, black lakes
    map.fillcontinents(color='#2d2d2d', lake_color='#000000')
    # black background
    map.drawmapboundary(fill_color='#000000')
    # thin white line for country borders
    map.drawcountries(linewidth=0.15, color="w")
    map.drawstates(linewidth=0.1, color="w")
    map.plot(lon, lat, linestyle='none', marker="o",
             markersize=25, alpha=0.4, c="white", markeredgecolor="silver",
             markeredgewidth=1)
    plt.text(-170, -72, 'Server locations of top 500 websites '
                        '(by traffic)\nPlot realized with Python and the Basemap'
                        ' library,issue Date'+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
             ha='left', va='bottom',
             size=28, color='silver')
    return fig


@app.route('/hello')
def hello():
    return  'hello'

@app.route('/')
def index():
    fig = getMap()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def main():
    app.run(port=7007,host='0.0.0.0')

if __name__ == '__main__':
    main()
