
"""
Author:
Purpose:
Date：
"""


import argparse
from urllib.request import urlopen
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def downloadFile():
    remotefile = None
    try:
        remotefile = urlopen('https://images-na.ssl-images-amazon.com/images/I/517+o9DVBqL._SX387_BO1,204,203,200_.jpg')
        #remotefile = urlopen('https://images-na.ssl-images-amazon.com/images/I/517+o9DVBqL._SX387_BO1,204,203,200')
    except:
        print('connection expcpt')
    localfile = open('n.jpg','wb')
    if remotefile:
         localfile.write(remotefile.read())
         remotefile.close()
    localfile.close()

def main():
    downloadFile()

if __name__ == '__main__':
    main()