#分模块测试，txt写入测试

# -*- coding: utf-8 -*-



# 这句话自带文件关闭功能，所以和那些先open再write再close的方式来说，更加pythontic！

# 如果写入中文 要设置编码

# a 表示追加文本内容
with open('douban.txt','a',encoding='utf-8') as f:
    f.write("豆瓣")