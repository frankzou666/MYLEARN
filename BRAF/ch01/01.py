"""
Author:
Purpose:
Date："""
import argparse
from flask import  Flask

app = Flask(__name__)

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

@app.route("/helloworld")
def helloWorld():
    return "hello horld!"

def main():
    """the entrance of this file"""
    app.run(host="0.0.0.0",port=5001,debug=True)


if __name__ == '__main__':
    main()
