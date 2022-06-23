
"""
Author:
Purpose:
Date：
"""


import argparse

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
base_url = 'http://www.webscrapingfordatascience.com/crawler/'
links_seen = set()

def visit(url, links_seen):

    html = requests.get(url).text
    html_soup = BeautifulSoup(html, 'html.parser')
    links_seen.add(url)
    for link in html_soup.find_all("a"):
        link_url = link.get('href')
        if link_url is None:
             continue
        full_url = urljoin(url, link_url)
        if full_url in links_seen:
            continue
    print('Found a new page:', full_url)






def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def main():
    visit(base_url, links_seen)

if __name__ == '__main__':
    main()