
"""
Author:
Purpose:
Date：
"""


import argparse
import requests

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
    url = 'http://www.webscrapingfordatascience.com/files/kitten.jpg'
    myheaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 ' + '(KHTML, like Gecko) Chrome / 61.0'
    }
    r = requests.get(url,headers = myheaders)
    print(r.status_code)
    with open('image.jpg','wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    main()