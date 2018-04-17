import re

'''
match.group([group1, ...])

　　获得匹配后的分组字符串，参数为编号或者别名；
	group(0)代表整个字符串，group(1)代表第一个分组匹配到的字符串，
	依次类推；如果编号大于pattern中的分组数或者小于0，则返回IndexError。
	另外，如果匹配不成功的话，返回None；如果在多行模式下有多个匹配的话，返回最后一个成功的匹配。
'''

m = re.match(r'(\w+)\s+(\w+)', 'Isaac Newton, physicist')
print(m)

print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

'''
match.groups(default=None)
返回一个tuple，包含所有的分组匹配结果；
如果default设为None的话，如果有分组没有匹配成功，则返回"None"；若设为0，则返回"0"。
'''

print(m.groups())




