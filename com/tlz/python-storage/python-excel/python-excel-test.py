# -*- coding:utf-8 -*-

# xlrd xlwt 用于读取2003版本的excel
import xlrd
import xlwt

# openpyxl 用于读写2007版本的excel
import openpyxl

from os import path

from xlutils.copy import copy

'''
2007版以前的Excel（xls结尾的），需要使用xlrd读，xlwt写。  xl-xls wt-write rd-read   
2007版以后的Excel（xlsx结尾的），需要使用openpyxl来读写。

保存文件时必须要有路径参数：否则
TypeError: save() missing 1 required positional argument: 'filename_or_stream'

'''

file_2003 = 'data/2003.xls'
file_2007 = 'data/2007.xlsx'

# 获取当前文件路径
current_path = path.dirname(__file__)
print(current_path)

# 写入excel的测试数据
value = [["名称", "价格", "出版社", "语言"],
         ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
         ["暗时间", "32.4", "人民邮电出版社", "中文"],
         ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]

value_test = [["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
              ["暗时间", "32.4", "人民邮电出版社", "中文"],
              ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]

a = ['1', '2', '3']
b = ['a', 'b', 'c']

for x, y in zip(a, b):
    data = {
        'num': x,
        'char': y
    }
    # print(data)


def write03_excel(current_path):
    wb = xlwt.Workbook()  # 创建一个excel工作簿对象
    sheet = wb.add_sheet('测试2003excel')  # 用工作普对象新建一个sheet
    # 二维的excel表格 所以需要一个双层for循环
    # 确定行列树  i,j list元素下标

    # for i in range(0, 4):
    #     for j in range(0, len(value[i])):
    #         sheet.write(i, j, value[i][j])  # 一个坐标放一个value

    #  这样给每一行数据加一个头  注意 循环的时候行要从1开始
    sheet.write(0, 0, "名称")
    sheet.write(0, 1, "价格")
    sheet.write(0, 2, "出版社")
    sheet.write(0, 3, "语言")

    for i in range(1, 4):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 一个坐标放一个value

    wb.save(current_path)
    print('写入数据成功！')


def read03_excel(file_2003):
    workbook = xlrd.open_workbook(file_2003)  # 打开一个excel工作簿 对象workbook

    # sheets = workbook.sheet_names();  # 获取工作簿中的sheet

    # worksheet = workbook.sheet_by_name(sheet[0]) # sheet[0] 输出的就是第一个sheet的名字

    worksheet = workbook.sheets()[0]  # 等价于上面两个

    rows_num = worksheet.nrows  # 读取行数
    cols_num = worksheet.ncols  # 读取列数

    for i in range(0, rows_num):
        for j in range(0, cols_num):
            print(worksheet.cell_value(i, j), '\t', end="")
        print()


def add_excel_data(file_2003):
    wb = xlrd.open_workbook(file_2003)  # 用wlrd提供的方法读取一个excel文件

    # sheets = wb.sheet_names()
    # sheet = wb.sheet_by_name(sheets[0])

    rows = wb.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数

    new_wb = copy(wb)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象

    new_sheet = new_wb.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet

    values = ["1", "2", "3"]

    for v in values:
        new_sheet.write(rows, 0, values)  # xlwt对象的写方法，参数分别是行、列、值

        new_sheet.write(rows, 1, 'hihi')
        new_sheet.write(rows, 2, 'haha')
    new_wb.save(file_2003)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel
    print('数据追加成功!')

if __name__ == '__main__':
    # write03_excel(file_2003)

    add_excel_data(file_2003)
    # read03_excel(file_2003)
