


"""
Author:
Purpose:
Date：
"""


import argparse
from flask import Flask


app = Flask(__name__)

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

@app.route('/hello')
def hello():
    return  '<h1>hello</he>'


def main():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0')

