
"""
Author:
Purpose:
Date：
"""


import argparse
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()



def hmtlParse():
    context = ssl._create_unverified_context()
    myurl = 'https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python'
    html = urlopen(myurl,context=context).read()
    soupified = BeautifulSoup(html,'html.parser')
    questions = soupified.find("div", {"class": "question"})
    questiontext = questions.find("div", {"class": "post-text"})
    print("Question: \n", questiontext.get_text().strip())




def main():
    hmtlParse()

if __name__ == '__main__':
    main()