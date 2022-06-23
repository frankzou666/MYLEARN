"""
Author:
Purpose:
Date：
"""

import argparse


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
    """
    t1 = tuple()
    t2 = ()
    t3 = (2, 1, 'a')
    t4 = 2, 1, 'a', 'a'
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    """
    """
    
    t5 = 2, 1, 'a', 'a','b','b','b'
    for i in set(t5):
        print('%s: %s'%(i, t5.count(i)))
    """
    """
    file = open('test.txt','w')
    for i in range(50):
        file.write(str(i)+'\n')
    file.close()

    
    
    with open('test.txt','r') as f:
        print(f.read())

    """
    """
    import pickle
    e = [1, 2, 3, 4]
    with open('dump.dat', 'wb') as f:
        pickle.dump(e, f)
    """
    """
    import pickle
    with open('dump.dat','rb') as f:
        e = pickle.load(f)
        print(e)
    """
    """
    import json
    dict1 = {'name':'frank', 'age':18}
    json.dump(dict1,fp=open('text.json','w'))

    restore_dict = json.load(fp=open('text.json', 'r'))
    print(restore_dict)
    
    """
    import csv
    file = csv.reader(open('1.csv'))
    for line in file:
        print(line)




if __name__ == '__main__':
    main()
