"""
Author:
Purpose:
Date："""
import argparse
import tensorflow_hub as hub
import ssl

import tensorflow_hub as hub
ssl._create_default_https_context = ssl._create_unverified_context

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
    print(hub.__version__)
    model = hub.KerasLayer("https://tfhub.dev/google/nnlm-en-dim128/2")
    embeddings = model(["The rain in Spain.", "falls","abc","def",
                        "mainly", "In the plain!"])

    print(embeddings.shape)  # (4,128)


if __name__ == '__main__':
    main()
