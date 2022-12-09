"""
Author:
Purpose:
Date："""
import argparse
import socket
import socket as sc
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
    HOST ="0.0.0.0"
    PORT =18888
    sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sc.bind((HOST,PORT))
    sc.listen(10)
    while True:
        connect, address = sc.accept()
        print(address)
        while True:
            data = connect.recv(1024)
            connect.send(b'Echo: '+data)
            if not data: break
        connect.close()


if __name__ == '__main__':
    main()
