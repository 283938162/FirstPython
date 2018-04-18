import pymysql
from DBUtils.PooledDB import PooledDB

'''
1.在程序创建连接的时候，可以从一个空闲的连接中获取，不需要重新初始化连接，提升获取连接的速度
2.关闭连接的时候，把连接放回连接池，而不是真正的关闭，所以可以减少频繁地打开和关闭连接
'''

hostname = '39.108.231.238'
port = 3306,
username = 'aliyun'
password = 'liu@2014'
dbname = 'DBTest'

# pool = PooledDB(pymysql, 5, hostname, username, password, dbname)


# 要按照参数形式来写
pool = PooledDB(creator = pymysql, mincached = 5, maxcached = 20, host = hostname, \
				user = username, passwd = password, db = dbname, charset = 'utf8')
conn = pool.connection()
cursor = conn.cursor()

# sql = "select * from emp"
sql = "update emp set empno = '%d' where ename = '%s'" % (1999, '张三丰')

try:
	# 执行sql
	# 使用 execute()  方法执行 SQL 查询
	r = cursor.execute(sql)  # 其返回值也是受影响的行数 与 rowcount属性一样

	print(r)
	# 获取所有记录的列表
	result = cursor.fetchall()

	print(result)
# for row in result:
# 	for col in range(len(row) - 1):
# 		print(row[col], end = '	')
# 	print()
except Exception as e:
	print("Error: unable to fetch data")
	print(e)

finally:
	cursor.close()
	conn.close()
