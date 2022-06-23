
import dir1
from imp import  reload

def main():
    print('main begin...')
    print('reload begin..')
    reload(dir1)
    print(dir1)


if __name__ == '__main__':
    main()
