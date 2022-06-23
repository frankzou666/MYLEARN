

import keras
from keras.preprocessing.text import  text_to_word_sequence,one_hot,hashing_trick,Tokenizer



def getOneHot():
    """

    :return:
    """
    tests = 'The quick brown fox ,jumped over the lazy dog.'
    results = set(text_to_word_sequence(tests))
    vocbsize = len(results)
    onehots = one_hot(tests, round(vocbsize * 1.3))
    print(vocbsize * 1.3)
    print(onehots)
    return  True


def getHashTricking():
    """

    :return:
    """
    tests = 'The quick brown fox ,jumped over the lazy dog.'
    results = set(text_to_word_sequence(tests))
    vocbsize = len(results)
    onehots = hashing_trick(tests, round(vocbsize * 1.3))
    print(vocbsize * 1.3)
    print(onehots)
    return True


def getTokenizer():
    """

    :return:
    """
    docs = ['Well done!',
            'Good work',
            'Great effort',
            'nice work',
            'Excellent!']
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(docs)
    print(tokenizer.word_counts)
    print(tokenizer.word_docs)
    print(tokenizer.word_index)
    print(tokenizer.document_count)



def main():
    getTokenizer()



if __name__ == '__main__':
    main()