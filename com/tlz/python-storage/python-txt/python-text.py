# 分模块测试，txt写入测试

# -*- coding: utf-8 -*-


# 这句话自带文件关闭功能，所以和那些先open再write再close的方式来说，更加pythontic！

# 如果写入中文 要设置编码

def open_write():

# a 表示追加文本内容
    with open('douban.txt', 'a', encoding='utf-8') as f:
        f.write("豆瓣")
#
#


def open_read():

    '''

    read() 读取全部文本，按文档原有的格式显现到控制台
    readline() 一次只读取一行 str
    readlines 读取多行 并将结果放到一个list钟，一行是一个元素


    '''
    file = open('douban.txt', encoding='utf-8').readlines()
    print(file)






open_read()
