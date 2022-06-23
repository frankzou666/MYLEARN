from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer


def getCountVectorize():
    text = ["The quick brown fox jumped over the lazy dog. The dog The fox"]
    countvectorizer = CountVectorizer()
    countvectorizer.fit(text)
    vector = countvectorizer.transform(text)
    print(countvectorizer.vocabulary_)
    return vector,countvectorizer


def getTDIDF():

    text = ["The quick brown fox jumped over the lazy dog.", "The dog", "The fox"]
    tfidfvectorizer = TfidfVectorizer()
    tfidfvectorizer.fit(text)
    vector = tfidfvectorizer.transform([text[0]])
    return vector, tfidfvectorizer



def getHashingVector():
    text = ["The quick brown fox jumped over the lazy dog"]
    hashingvectorizer = HashingVectorizer(n_features=20)
    vector = hashingvectorizer.transform(text)
    return vector, hashingvectorizer

def main():
    vector, hashingvectorizer = getHashingVector()
    print(vector.shape)
    print(vector.toarray())


if __name__ == '__main__':
    main()
