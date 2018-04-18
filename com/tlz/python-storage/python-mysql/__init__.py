import pymysql

# 打开数据库连接
db = pymysql.connect("39.108.231.238", "aliyun", "liu@2014", "DBTest", charset = 'utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 创建表
# cursor.execute("drop table if EXISTS tt")
#
# sql_createTabel = '''
#
# create table tt(
# id int auto_increment PRIMARY KEY,
# name VARCHAR(50),
# age int(10)
# )
# '''
#
# cursor.execute(sql_createTabel)
# print("创建表成功！")

# 插入

# sql_insert = "insert into tt(name,age) VALUES ('张三丰',110)"
#
#
# try:
# 	for x in range(10):
# 		cursor.execute(sql_insert)
#
# 	# 提交
# 	db.commit()
# 	print("插入成功")
# 	print(cursor.rowcount)
# except Exception as e:
# 	print(e)
# 	db.rollback()


# 更新
sql_update = "update emp set empno = '%d' where ename = '%s'" % (111, '张三丰')

# "update emp set empno = '%d' where ename = '%s'" % (1999, '张三丰')
#
try:
	cursor.execute(sql_update)
	db.commit()

	print("更新成功！")
except Exception as e:
	print(e)
	db.rollback()


# 删除

# sql_delete = "delete from emp where empno = '%d'"%(1000)
#
# try:
# 	cursor.execute(sql_delete)
# 	db.commit()
#
# 	print("删除成功！")
# except Exception as e:
# 	print(e)
# 	db.rollback()


# 查询
# sql语句
sql = "select * from emp where sal > '%s' and job = '%s' and hiredate BETWEEN '%s' and '%s' and ename like '%s'" % (
	10000, '销售员', '2001-02-01', '2001-02-29', '殷%')  # 这样写也可以 但是

sql2 = "select * from emp where sal > '%d' and job = '%s' and hiredate BETWEEN '%s' and '%s' and ename like '%s'"

# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()


# 默认打印所有字段的数据
# try:
# 	# 执行sql
# 	# 使用 execute()  方法执行 SQL 查询
# 	cursor.execute(sql)  # 其返回值也是受影响的行数 与 rowcount属性一样
#
# 	# 获取所有记录的列表
# 	result = cursor.fetchall()
# 	for row in result:
# 		for col in range(len(row) - 1):
# 			print(row[col], end = '	')
# 		print()
# except:
# 	print("Error: unable to fetch data")


# 打印指定字段的数据
#
# try:
# 	cursor.execute(sql)
# 	# cursor.execute(sql2, (10000, '销售员', '2001-02-01', '2001-02-29', '殷%'))  # 这种写法| 有问题
# 	result = cursor.fetchall()  # 返回的是一个元组类型
#
# 	for row in result:
# 		# print(row)
# 		empno = row[0]
# 		ename = row[1]
# 		job = row[2]
#
# 		hiredate = row[4]
# 		sal = row[5]
# 		# comm = row[6]  有NULL值存在
#
# 		# python 格式化 输出  s 字符型 d 整形 f 带小数点
# 		print("empno = %d,ename= %s,job=%s,hiredate=%s,sal=%.2f" % (empno, ename, job, hiredate, sal))
#
# except Exception as e:
# 	print("Error: unable to fetch data")
# 	print(e)

#
# print ("Database version : %s " % num)

# 关闭数据库连接
db.close()
