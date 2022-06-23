

import os
import re
import nltk
import string
from collections import Counter

def loadfile(path):
    """
    :func: load file to line
    :param path:
    :return:
    """
    file=open(path,'r')
    line=file.read()
    file.close()
    return line

def loadpath(path,vocab):
    for file in os.listdir(path):
        if not file.endswith('.txt'):
            continue
        addvocab(os.path.join(path,file),vocab)


def addvocab(file,vocab):
    texts = loadfile(file)
    tokens = custoke(texts)
    vocab.update(tokens)

def custoke(texts):
    tokens = texts.split()
    # remove the string.pnctuation
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    tokens = [re_punc.sub('', w) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    return tokens



def doctoline(filename, vocab):
    doc = loadfile(filename)
    tokens = custoke(doc)
    tokens = [w for w in tokens if w in vocab]
    return ' '.join(tokens)

def processtodoc(path,vocab):
    lines= list()
    for file in os.listdir(path):
        if not file.endswith('.txt'):
            continue
        line =   doctoline(os.path.join(path,file),vocab)
        lines.append(line)
    return lines

def savelist(lines,filename):
    data='\n'.join(lines)
    file=open(filename,'w')
    file.write(data)
    file.close()


def main():
    NEGBASEPATH = 'C:\\1\\movie\\review_polarity\\txt_sentoken\\neg'
    POSBASEPATH = 'C:\\1\\movie\\review_polarity\\txt_sentoken\\pos'
    vocab =Counter()
    loadpath(NEGBASEPATH,vocab)
    loadpath(POSBASEPATH, vocab)
    min5token= [k for k ,v in vocab.items() if v>5]
    negativelines=processtodoc(NEGBASEPATH,vocab)
    savelist(negativelines,'C:\\1\\movie\\review_polarity\\neg.txt')
    posativelines = processtodoc(POSBASEPATH, vocab)
    savelist( posativelines, 'C:\\1\\movie\\review_polarity\\pos.txt')




if __name__ == '__main__':
    main()