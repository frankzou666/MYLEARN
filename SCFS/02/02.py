"""
Author:
Purpose:
Date：
"""

import argparse
import requests
import time


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main1():
    """the entrance of this file"""
    urlpath = 'http://127.0.0.1:5000/myapp/api/books'
    headers = {
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NDM0MDY2OCwianRpIjoiZWEyMDY5MjctNDJhNi00YjE2LWJkM2UtZDk5NjcwNWJlZGE1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImZyYW5rIiwibmJmIjoxNjQ0MzQwNjY4LCJleHAiOjE2NDQzNzY2Njh9.Eyggb-dALp__3LAVs4OjSCHTaPxoagQO9BqDL-O2TEk'
    }
    while True:
        rsp = requests.get(url=urlpath, headers=headers)
        result = rsp.json()
        time.sleep(2)
        print(result)

def fun1(i):
    if i == 1:
        print(i)
    else:
       i = i-1
       fun1(i)
    return True

def main():
    fun1(10)


if __name__ == '__main__':
    main()
