import re

'''
正则表达式对象
通过 re.compile() 我们可以得到一个编译的正则表达式对象，

'''


# regex.search(string[, pos[, endpos]])  pos 开始位置 endpos结束位置

# 对整个字符串进行搜索，并返回第一个匹配的字符串的match对象。
def regex_search():
	pattern = re.compile(r'd')
	regex = pattern.search('dog')
	print(regex)


# regex_search()

# regex.match(string[, pos[, endpos]])
# 从字符串“开头”去匹配，并返回匹配的字符串的match对象。匹配不到时，返回None
def regex_match():
	pattern = re.compile('d')
	regex = pattern.match('dog')
	print(regex)

# regex_match()

# def regex_():
# def regex_():
#
# def regex_():


