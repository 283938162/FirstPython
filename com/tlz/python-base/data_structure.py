# list 嵌套
# lists = []
# list=[]
#
# a = 'a'
# b = 'b'
# list.append(a)
# list.append(b)
#
# lists.append(list)
# print(list)
# print(lists)

# 多层循环

a = ['a', 'b']
b = ['b', 'c']
c = ['c', 'd']

for x, y, z in zip(a, b, c):
    k = x
    l = y
    t = z
    print(k, l, z)
