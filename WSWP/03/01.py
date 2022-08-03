"""
Author:
Purpose:
Date：
"""

import argparse
from urllib.request import  urlopen
from bs4 import BeautifulSoup
import ssl

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
    context = ssl._create_unverified_context()
    url_path = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
    res = urlopen(url=url_path, context=context)
    bs = BeautifulSoup(res, 'html.parser')
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link)


if __name__ == '__main__':
    main()
