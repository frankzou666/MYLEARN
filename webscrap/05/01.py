
"""
Author:
Purpose:
Date：
"""


import argparse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


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
    url = 'http://www.webscrapingfordatascience.com/postform2/'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    input('Press ENTER to close the automated browser')
    driver.quit()




if __name__ == '__main__':
    main()