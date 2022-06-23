
"""
Author:
Purpose:
Date：
"""


import argparse
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main2():
    X,y = make_moons(n_samples=5000,noise=0.3)
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,random_state=20)
    svcclf = SVC(probability=True)
    randomForestClassifierclf = RandomForestClassifier(n_estimators=500)
    logisticRegressionclf = LogisticRegression()
    votingClassifier = VotingClassifier(estimators=[('svcclf',svcclf ),
                                                    ('randomForestClassifierclf', randomForestClassifierclf),
                                                    ('logisticRegressionclf',logisticRegressionclf)
                                                    ],
                                        voting='hard')
    for clf in (svcclf,randomForestClassifierclf , logisticRegressionclf,votingClassifier):
        clf.fit(Xtrain,ytrain)
        ypred = clf.predict(Xtest)
        print(clf.__class__.__name__,accuracy_score(ytest,ypred))


def main3():
    X,y = make_moons(n_samples=1000,noise=0.4)
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,random_state=20)
    baggingClassifier  =  BaggingClassifier(DecisionTreeClassifier(),n_estimators=500,n_jobs=10,bootstrap=True,max_samples=50)
    randomForestClassifier = RandomForestClassifier(n_estimators= 500,n_jobs= -1)
    for clf in (baggingClassifier, randomForestClassifier):
        clf.fit(Xtrain, ytrain)
        ypred = clf.predict(Xtest)
        print(clf.__class__.__name__, accuracy_score(ytest, ypred))


def getVoteClassifier():
    """
    :return:
    """
    X,y = make_moons(n_samples=5000,noise=0.3)
    Xtrain,Xtest,ytrain,ytest= train_test_split(X,y,shuffle=True,random_state=1,test_size=0.2)
    #svcclssifier
    svcclf = SVC()
    # logistic
    lgclf = LogisticRegression()
    #randomforest
    randomforestclf = RandomForestClassifier()
    #voteclassifier
    voteclf = VotingClassifier(estimators=[
        ('svcclf',svcclf),
        ('lgclf', lgclf),
        ('randomforestclf', randomforestclf)
    ], voting='hard')
    # diffieece classifier
    for clf in (svcclf, lgclf,  randomforestclf,voteclf):
        clf.fit(Xtrain, ytrain)
        ypred = clf.predict(Xtest)
        print('%s:%s'%(clf.__class__.__name__,accuracy_score(ytest, ypred)))


def getBaggingClassifier():
    """

    :return:
    """
    X, y = make_moons(n_samples=5000, noise=0.3)
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, shuffle=True, random_state=1, test_size=0.2)
    # svcclssifier
    svcclf = SVC()
    # logistic
    lgclf = LogisticRegression()
    # randomforest
    randomforestclf = RandomForestClassifier()
    # voteclassifier
    voteclf = VotingClassifier(estimators=[
        ('svcclf', svcclf),
        ('lgclf', lgclf),
        ('randomforestclf', randomforestclf)
    ], voting='hard')
    baggingstrapclf = BaggingClassifier(DecisionTreeClassifier(),
                                        n_estimators=500,
                                        bootstrap=True,
                                        max_samples=100,
                                        oob_score=True,
                                        n_jobs=-1)
    adaboosting = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                                     n_estimators=500,
                                     learning_rate=0.5)
    for clf in (lgclf, voteclf, baggingstrapclf,adaboosting):
        clf.fit(Xtrain, ytrain)
        ypred = clf.predict(Xtest)
        print('%s:%s' % (clf.__class__.__name__, accuracy_score(ytest, ypred)))
    return  True


def main4():
    X,y = make_moons(n_samples=1000,noise=0.4)
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,random_state=20)
    adaBoostClassifier  =  AdaBoostClassifier(DecisionTreeClassifier(),
                                                algorithm='SAMME.R',
                                                n_estimators=100,
                                                learning_rate= 0.5)
    randomForestClassifier = RandomForestClassifier(n_estimators= 500,n_jobs= -1)

    for clf in (adaBoostClassifier, randomForestClassifier):
        clf.fit(Xtrain, ytrain)
        ypred = clf.predict(Xtest)
        print(clf.__class__.__name__, accuracy_score(ytest, ypred))


def main():
    getBaggingClassifier()

if __name__ == '__main__':
    main()