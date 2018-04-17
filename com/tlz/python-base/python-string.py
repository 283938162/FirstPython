'''
replace
'''
# s='http://shp.qpic.cn/ishow/2735012211/1516590356_84828260_8310_sProdImgNo_2.jpg/200'
#
# ss=s.replace('/200','/0')
#
# print(s)
# print(ss)
# print(s[:-3]+'0')


'''
split
'''
# a = '恋之微风|万圣前夜|天鹅之梦|纯白花嫁|缤纷独角兽'
#
#
# a_all = a.split('|')
#
# print(a_all)
#


'''
count

S.count(sub[, start[, end]]) -> int

'''

# 如何精确匹配a 出现的次数
import re

html = 'a bb cc  dd  cc  cc ad  bb cc'

print(html.count('a', 0, len(html)))

print(len(re.findall(r'()', html)))
