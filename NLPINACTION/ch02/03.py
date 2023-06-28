"""
Author:
Purpose:
Date："""
import argparse
import  numpy as np
import pandas as pd

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
    sent = """Thomas Jefferson began hi building Monticello at the 26."""
    toke_seqn = sent.split()
    # 生成所有词的一个相当于dict
    vocab = sorted(set(toke_seqn))
    num_tokens = len(toke_seqn)
    vocab_size = len(vocab)
    # 初始化
    onehot_vector = np.zeros((num_tokens, vocab_size))
    # 对应的行和列上设为1
    for i, word in enumerate(toke_seqn):
        onehot_vector[i, vocab.index(word)] = 1
    print(onehot_vector)
    pd1 = pd.DataFrame(onehot_vector,columns=vocab)
    print(pd1.0)


if __name__ == '__main__':
    main()

