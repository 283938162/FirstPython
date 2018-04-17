import re



'''
 
 输出特定字符开始或者结尾的字符串
 
'''


var1 = '>123abc78<zha>'

var = re.findall('<[^>]*>',var1)

print(var)




'''
python re.sub属于python正则的标准库,主要是的功能是用正则匹配要替换的字符串
然后把它替换成自己想要的字符串的方法
re.sub 函数进行以正则表达式为基础的替换工作
精确替换使用replace方法

'''

# var = '1f436ff love 网吧 people'

# var2 = '人生难得一只鸡！< =" 1f436"></>'
# var1 = re.sub(r'<[^>]*>', '', var2)
#
# print(var1)

# var = '赞(5)'


# 在Python中，None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False。除此之外的其它对象都会被转化成True
# print(re.findall(r'\d+', var) )
#
# if re.findall(r'\d+', var):
#     like = re.findall(r'\d+', var)[0]
# else:
#     like = 0
#
#
# print(like)
# print(var1)
# print(var1.strip())


# a="/song?id=354976"
#
# print(type(a))
# print(filter(str.isdigit(),a))

# string = '/song?id=354976'
# # string2 = string.encode('gbk')
# print(type(str))
# print(filter(str.isdigit, '123asd'))

# ly = """
# [00:28.690]往事不要再提
# [00:32.170]人生已多风雨
# [00:36.580]纵然记忆抹不去
# [00:38.670]爱与恨都还在心里
# [00:43.840]真的要断了过去
# """
# print(ly)
#
# pat = re.compile(r'\[.*\]')
# lrc = re.sub(pat,"",ly)
# print(lrc.strip())
