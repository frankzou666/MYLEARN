
from collections import Counter

def main():
    countr = Counter("hello world, i am first, hello".split())
    print(dict(countr.items()))

if __name__ == '__main__':
    main()