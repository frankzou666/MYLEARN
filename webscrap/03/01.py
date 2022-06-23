
"""
Author:
Purpose:
Date：
"""


import argparse
import requests
from bs4 import BeautifulSoup

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
    url = 'https://en.wikipedia.org/w/index.php' + \
          '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
    r = requests.get(url)
    bs = BeautifulSoup(r.text,'html.parser')
    for item in bs.select('li.toclevel-2'):
        link = item.find('a')
        print(link.get_text())
        print(url+link.attrs['href'])


if __name__ == '__main__':
    main()