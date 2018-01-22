import re

var = '赞(5)'


# 在Python中，None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False。除此之外的其它对象都会被转化成True
print(re.findall(r'\d+', var) )

if re.findall(r'\d+', var):
    like = re.findall(r'\d+', var)[0]
else:
    like = 0


print(like)
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