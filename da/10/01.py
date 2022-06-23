
import datetime
import pandas as pd



def main():
    t = pd.date_range('2021-06-01 00:00:00','2021-08-01 00:00:00',freq='1W')
    print(list(t))


if __name__ == '__main__':
    main()