#coding:utf-8

import xlsxwriter

xl = xlsxwriter.Workbook(r'E:\Git\Practice\y16m9_practice\XL.xlsx')
table = xl.add_worksheet('sheet1')
table.write_string(0, 0, U'Excel测试')
for i in range(2, 52):
    cell = 'A' + str(i)
    table.write_string(cell, 'test' + str(i-1))
xl.close()