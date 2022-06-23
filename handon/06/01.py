
"""
Author:
Purpose:
Date：
"""


import argparse
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,export_graphviz

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
    iris = load_iris()
    X = iris.data[:,2:]
    y = iris.target
    treeclf = DecisionTreeClassifier(max_depth=2)
    treeclf.fit(X,y)
    export_graphviz(
        treeclf,
        out_file= "iris_tree.dot",
        feature_names=iris.feature_names[2:],
        class_names=iris.target_names,
        rounded=True,
        filled=True
    )



if __name__ == '__main__':
    main()