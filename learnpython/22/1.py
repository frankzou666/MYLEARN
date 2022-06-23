
import test
from imp import reload

def main():
    test.f()
    reload(test)


if __name__ == '__main__':
    main()