
"""
Author:
Purpose:
Date：
"""


import argparse
from http.server import HTTPServer,CGIHTTPRequestHandler
from http.cookies import  SimpleCookie

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
    httpserver = HTTPServer(('',80),CGIHTTPRequestHandler)
    httpcookie = SimpleCookie()
    httpcookie['name'] = 'frank'
    print(httpcookie.output())
    httpserver.serve_forever()

if __name__ == '__main__':
    main()