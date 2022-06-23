"""
Author:
Purpose:
Date：
"""

import argparse
import sqlite3
from flask import Flask
from flask import request,render_template,jsonify

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


@app.route('/hello')
def test():
    return '<h1>hello world</he>'


@app.route('/post', methods=['POST'])
def getPost():
    print(request.get_json())
    return jsonify({'msg':'ok'}) ,201


def createDb():
    db = sqlite3.connect('test.db')
    db.execute('create table t1(id int,name varchar(100))')

def insertDb():
    db = sqlite3.connect('test.db')
    cursor = db.cursor()
    cursor.execute('insert into t1(id,name) values(10,\'frank\')')
    cursor.execute('insert into t1(id,name) values(2,\'smith\')')
    db.commit()
    db.close()

def delDb():
    db = sqlite3.connect('test.db')
    cursor = db.cursor()
    cursor.execute('delete from t1')
    db.commit()
    db.close()

def getDb():
    db = sqlite3.connect('test.db')
    cursor = db.cursor()
    cursor.execute('select *  from t1')
    res = cursor.fetchall()
    db.close()
    return  res

def main():
    insertDb()
    print(getDb())
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
