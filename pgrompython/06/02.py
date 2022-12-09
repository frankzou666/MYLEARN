"""
Author:
Purpose:
Date："""
import argparse
import sys,glob,os
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def getBiggestFile():
    """the entrance of this file"""
    DIR = os.getcwd()
    file_list = []
    for file in glob.glob(DIR+os.sep+"*.py"):
        file_size = os.path.getsize(file)
        file_list.append((file_size,file))
    file_list.sort(reverse=True)
    print(file_list)


def main():
    import sys, os, pprint
    trace = False
    if sys.platform.startswith('win'):
        dirname = r'C:\Python31\Lib'
    else:
        dirname = '/Users/zoufrank/Documents/dev/py/MYLEARN/pgrompython/'
        # Windows
        # Unix, Linux, Cygwin
    allsizes = []
    for (thisDir, subsHere, filesHere) in os.walk(dirname):
            if trace: print(thisDir)
            for filename in filesHere:
                if filename.endswith('.py'):
                    if trace: print('...', filename)
                    fullname = os.path.join(thisDir, filename)
                    fullsize = os.path.getsize(fullname)
                    allsizes.append((fullsize, fullname))
    allsizes.sort()
    pprint.pprint(allsizes)
    #pprint.pprint(allsizes[-2:])



if __name__ == '__main__':
    main()
