
import pandas as pd

def main():
    pr = pd.date_range('2023-01-01','2024-10-01')
    date_list = pr.values
    for i in range(len(date_list)-1):
        print(date_list[i],date_list[i+1])



if __name__ == '__main__':
    main()