"""
Author:
Purpose:
Date：
"""

import argparse
from urllib.request import  urlopen
from bs4 import BeautifulSoup
import ssl
from urllib.error import  HTTPError

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main():
    """the entrance of this file"""
    URL1 ="http://www.pythonscraping.com/pages/page3.html"

    URLS = [URL1]
    for URL in URLS:
       context = ssl._create_unverified_context()
       try:
           html = urlopen(URL, context=context)
           bs = BeautifulSoup(html, 'html.parser')
           for item in bs.find('table', {'id':'giftList'}):
               print(item)
       except HTTPError as e:
           print(URL+': '+e.__str__())
       except Exception as e:
           print(URL+': '+e.__str__())


if __name__ == '__main__':
    main()
