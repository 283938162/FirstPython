import re

var = 'Hello World!'

'''
re.search(pattern, string, flags=0)

　　　　对整个字符串进行搜索，并返回第一个匹配的字符串的match对象。

　　　　pattern : 使用的正则表达式 

　　　　string :  要匹配的字符串

　　　　flags : 用来控制正则表达式的匹配规则。比如是否区分大小写
'''

# print(re.search(r'e',var))
# <_sre.SRE_Match object; span=(1, 2), match='e'>


'''
re.match(pattern, string, flags)
　　　　从字符串“开头”去匹配，并返回匹配的字符串的match对象。匹配不到时，返回None
'''

# print(re.match(r'e',var))
# None

# print(re.match(r'He',var))
# <_sre.SRE_Match object; span=(0, 2), match='He'>


'''
re.fullmatch(pattern, string, flags=0)

　　　　如果正则表达式匹配整个字符串，则返回匹配到的match对象， 否则返回None。 注意这里不同于0长度的匹配。
'''

# print(re.match(r'e','eeee'))
# print(re.fullmatch(r'e','eeee'))
# print(re.fullmatch(r'e+','eeee'))
#
# print(re.fullmatch(r'[a-z]', 'a'))
# print(re.fullmatch(r'[a-z]', 'ab'))
# print(re.fullmatch(r'[a-z]+', 'a'))
# print(re.fullmatch(r'[a-z]+', 'abcdef'))
# print(re.fullmatch(r'[a-z\s]+', 'abc def'))
# print(re.fullmatch(r'[a-z\s\<]+', 'abc de  <'))

'''
re.findall(pattern, string, flags=0)

　　　　返回一个所有匹配的字符串的字符串列表
'''

# print(re.findall(r'a','here where >.<'))
# print(re.findall(r'e','here where >.<'))


'''
　　re.sub(pattern, repl, string, count=0, flags=0)

　　　　使用repl替换string中每一个匹配的子串后返回替换后的字符串。 

　　　　当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
　　　　当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
　　　　count用于指定最多替换次数，不指定时全部替换。

'''

print(re.sub(r'\d+', '', 'abc 123, hello 456.'))


#  正则表达式对象
pattern = re.compile(r'\d+')
var = pattern.sub('', 'abc 123, hello 456.')
print(var)

'''
 
 正则表达式对象
 
'''
