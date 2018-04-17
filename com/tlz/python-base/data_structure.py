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
#
# a = ['a', 'b']
# b = ['b', 'c']
# c = ['c', 'd']
#
# for x, y, z in zip(a, b, c):
#     k = x
#     l = y
#     t = z
#     print(k, l, z)


'''
 S.join(iterable) -> str
'''

# 将集合拼接成字符串 '这里是间隔符号' ''空格隔开  '-'横杠隔开
# a = ['a','b','c']
# print('-'.join(a))
#
#
# # 高效的写法  意思是：进入for循环 然后进行for之前的操作  1=4的操作
# b = [x+'_' for x in a[2:]]
#
#
# bb = []
# for x in a[2:]:
#     bb.append(x+'_')
# print(bb)


# 等价于：
# print(b)

'''
sort
'''

l = [('sara', 80,12), ('sbbbbra', 80,34),('mary', 90,45), ('lily', 95,6), ('david', 90,123)]

# 若果不指定排序规则  则按字典顺序
l.sort()
print(l)