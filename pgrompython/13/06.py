"""
Author:
Purpose:
Date："""
import argparse
import http.client
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
    servername, filename = 'www.163.com','/index.html'
    print(servername, filename)
    server = http.client.HTTPConnection(servername)
    server.putrequest('GET', filename)
    server.putheader('Accept', 'text/html')
    server.endheaders()
    reply = server.getresponse()
    if reply.status != 200:
        print('server connect error...',reply.status)
    data = reply.readlines()
    reply.close()
    for line in data:
        print(data)


# cmdline args? '/index.html'


if __name__ == '__main__':
    main()
