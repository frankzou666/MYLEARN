
"""
Author:
Purpose:
Date：
"""


import argparse
from nltk.translate.bleu_score import  sentence_bleu

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
    cid =['this','ok', 'is', 'a','test']
    ref = [['this', 'is', 'test'],['this', 'is', 'a', 'test']]
    bleuscore = sentence_bleu(ref,cid,weights=(0,1,0,0))
    print(round(bleuscore,10))


if __name__ == '__main__':
    main()