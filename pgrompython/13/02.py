
"""
Author:
Purpose: ftplib client
Date："""
from ftplib import FTP
import argparse

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main():
    """the entrance of this file"""
    userinfo = ('lutz','Pswd?')
    sitename = 'ftp.rmi.net'
    connection = FTP(sitename,timeout=20)
    connection.login(userinfo)


if __name__ == '__main__':
    main()
