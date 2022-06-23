

import numpy as np
import gensim
from gensim.models import Word2Vec



def main():
    sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
                 ['this', 'is', 'the', 'second', 'sentence'],
                 ['yet', 'another', 'sentence'],
                 ['one', 'more', 'sentence'],
                 ['and', 'the', 'final', 'sentence']]
    # train model
    model = Word2Vec(sentences, min_count=1)
    # summarize the loaded model
    print(model)
    # summarize vocabulary
    #words = list(model.wv.index_to_key())
    print(model.wv._upconvert_old_vocab)
    # access vector for one word

if __name__ == '__main__':
    main()