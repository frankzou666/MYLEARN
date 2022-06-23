
from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import nltk


def getBag():
    """
    :return:
    """
    vectors = []
    sentence = """The faster Harry got to the store, the faster Harry,
... the faster, would get home."""

    treebankwordtokenizer = TreebankWordTokenizer()
    tokens = treebankwordtokenizer.tokenize(sentence.lower())
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [token for token in tokens if token not in stopwords]
    counter = Counter(tokens)
    countlen= len(counter)
    for key, value in counter.most_common():
        vectors.append(value/countlen)
    print(vectors)
    return True

def main():
    getBag()

if __name__ == '__main__':
    main()