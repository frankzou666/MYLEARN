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
    URL1 ="http://www.pythonscraping.com/pages/page1"
    URL2 = "http://www.pythonscraping.com/pages/page1.html"
    URL3 = "http://www.ddd3434dfsafwer.com"
    URLS = [URL1, URL2,URL3]
    for URL in URLS:
       context = ssl._create_unverified_context()
       try:
           html = urlopen(URL, context=context)
           bs = BeautifulSoup(html, 'html.parser')
           print(bs.h1)
       except HTTPError as e:
           print(URL+': '+e.__str__())
       except Exception as e:
           print(URL+': '+e.__str__())


if __name__ == '__main__':
    main()
