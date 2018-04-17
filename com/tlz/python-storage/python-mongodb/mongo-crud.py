from pymongo import MongoClient

server_ip = '39.108.231.238'
server_port = 27017

'''
区分属性和方法
'''

conn = MongoClient(server_ip, server_port)

new_db = conn.new_mydb

new_col = new_db.new_mycol

book_info = [{'name': 'Java指南', 'price': 300000, 'tag': 'tech'}, {'name': '寻梦环游记', 'tag': 'moive','price': 30,},
			 {'name': 'Mac', 'tag': '3C','price': 3}, {'name': 'iPhone', 'tag': '3C','price': 3000000,}]

# 有则更新 无责插入


for book in book_info:

	# if new_col.find_one({'name': book['name']}):
	# 	print('这个数据存在 更新吧')
	# else:
	# 	print('没有这个数据，插入吧')

	flag = new_col.find_one({'name': book['name']})
	print('flag=%s,book[\'name\']=%s' % (flag, book['name']))

	if flag:
		print('这个数据存在 更新吧 flag =%s' % flag)
		new_col.update({'name': book['name']}, {'$set': {'price': book['price']}})
	else:
		print('没有这个数据，插入吧 flag =%s' % flag)
		new_col.insert(book)

# 查询不存在的数据
# find与 find_one的区别

print(new_col.find_one({'name': 'Mac'}))  # 不存在的数据 返回 None
print('find = %s' % new_col.find({'name': 'Mac'}))  # 不存在数据 返回并不会None

print('数量=%s' % new_col.find({'name': 'Mac'}).count())
for i in new_col.find({'name': 'Mac'}):
	print('i = %s' % i)

# 插入
# new_col.insert(book_info)
# new_col.insert_one({'name': 'Alice', 'tag': 'noval'})
# new_col.insert_many([{'name': 'Python指南', 'price': 45, 'tag': 'tech'},{'name': 'C++指南', 'price': 40, 'tag': 'tech'}])

# 查询
for i in new_col.find():
	print(i)
#
# for i in new_col.find({'name': 'Java指南'}):
#     print(i)
#
# print(new_col.find_one())
# print(new_col.find()[1])


#  And的内容只能写在一个里面
# print('*********')

# for i in new_col.find({'tag': 'tech'}):
#     print(i)

# OR 的写法

# for i in new_col.find({'$or': [{'name': 'Alice'}, {'tag': 'moive'}]}):
#     print(i)

# 条件操作符
# for i in new_col.find({'price': {'$gte': 40}}):
#     print(i)


# And OR

# for i in new_col.find({'tag': 'tech', 'price': {'$gte': 40}, '$or': [{'name': 'Alice'},{'name':'C++指南'},{'tag': 'moive'}]}):
#     print(i)
#

#
# 更新
# new_col.update({'tag': 'noval'}, {'$set': {'tag': 'xiaoshuo'}})
#
# print(new_col.find_one({'name': 'Alice'}))

# 删除

# id = new_col.find_one({'name': 'Alice'})['_id']
# print('id = %s' % id)

# new_col.remove({'_id': id})

# new_col.remove(id)
# print('id = %s' % id)
