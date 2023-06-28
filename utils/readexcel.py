"""
Author:
Purpose:
Date：
"""

import argparse
import xlrd



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
    file_path = 'data.xlsx'
    sql_file =  'data.sql'
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[0]
    file = open(sql_file,'w',encoding='utf8')
    print('input xlsx file: '+file_path)
    for rown in range(1,table.nrows):
        str0 = table.cell_value(rown, 0)
        str1 = table.cell_value(rown, 1)
        str2 = table.cell_value(rown, 2)
        str3 = table.cell_value(rown, 3)
        str4 = table.cell_value(rown, 4)
        str5 = table.cell_value(rown, 5)
        sql_str='insert into sv() values (\'%s\',\'%s\', \'%s\',\'%s\',\'%s\',,\'%s\');'%(str0,str1,str2,str3,str4,str5)
        print(sql_str,file=file)
        #file.write(sql_str)
    file.close()
    print('ouput sql file: ' + sql_file)



if __name__ == '__main__':
    main()
