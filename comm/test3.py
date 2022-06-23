
from configparser import ConfigParser
from flask import current_app,g


"""
测试类
"""


class TestLog():
    def __init__(self):
        self.teststr = 'hello Testlog'
        self.configparser= ConfigParser()
        self.configparser.read('config.ini')
        print(current_app.config['HOST'])
        print('TESTLog被创建...')

    def getTestStr(self):

        print('TestLog.getStr()被调用了....')
        return self.teststr

    def getDbHost(self):
        print(self.configparser.get('db','host'))
        return  self.configparser.get('db','host')



def getTestLog():
    testLog = TestLog()
    return testLog