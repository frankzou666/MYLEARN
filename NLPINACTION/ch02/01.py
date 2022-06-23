
"""
Author:
Purpose:
Date：
"""


import argparse
from collections import Counter
import collections
from  vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nlpia.data.loaders import get_data


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def sentimentFunc():

    sa  = SentimentIntensityAnalyzer()
    corpus = [
        'i am not bad',
        'bad',
        'i am angry',
        'so bad'
    ]
    for doc in corpus:
        score = sa.polarity_scores(doc)
        print('{}:{}'.format(doc,score['compound']))





def main():
    movies = get_data('hutto_movies')
    movies = movies[0:1000]
    import pandas as pd
    from collections import Counter
    from nltk.tokenize import casual_tokenize
    bagofwords =[]
    for text  in movies.text[0:1000]:
        bagofwords.append(Counter(casual_tokenize(text)))
    df = pd.DataFrame.from_records(bagofwords)
    df = df.fillna(0).astype(int)

    from sklearn.naive_bayes import  MultinomialNB
    nb = MultinomialNB()
    nb.fit(df,movies[0:1000].sentiment>0)
    # what is this
    movies['predicted_sentiment'] = nb.predict(df) * 8 - 4
    movies['error'] = (movies.predicted_sentiment - movies.sentiment).abs()
    print(movies.error.mean().round(1))


if __name__ == '__main__':
    main()