"""
Author:
Purpose:
Date：
"""

import argparse


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', metavar='name', default='world!', help='name message')
    return argparser.parse_args()

def clean_text():
    """

    :return:
    """
    pass


def  preprocess_input():
    """

    :return:
    """
    pass



def get_suggestions():
    """

    :return:
    """
    pass



def main():
    """the entrance of this file"""
    input_text = getargs()
    process_text = clean_text()
    tokenizer_sentence = preprocess_input()
    suggestion = get_suggestions()





if __name__ == '__main__':
    main()
