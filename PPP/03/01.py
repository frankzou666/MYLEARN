"""
Author:
Purpose: automatic invoice generation
Date：
"""

import argparse
import flask


import os

os.environ['FONTCONFIG_FILE'] = r'C:\Program Files\GTK2-Runtime Win64\etc\fonts\fonts.conf'



from weasyprint import HTML
#os.environ['FONTCONFIG_PATH'] = r'C:\Windows'





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
    #html = HTML('invoice.html')
    #html.write_pdf('invoice.pdf')
    print(os.environ['PATH'])


if __name__ == '__main__':
    main()
