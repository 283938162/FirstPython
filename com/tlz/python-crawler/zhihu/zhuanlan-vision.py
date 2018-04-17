from pymongo import MongoClient
from pyecharts import Funnel  # 漏斗图


def init_mongodb():
	settings = {
		"ip": '39.108.231.238',  # ip
		"port": 27017,  # 端口
		"db_name": "zl_db",  # 数据库名字
		"set_name": "zl_set"  # 集合名字
	}

	# 建立数据库连接
	conn = MongoClient(settings['ip'], settings['port'])

	# 建立数据库和集合
	zl_db = conn[settings['db_name']]
	zl_set = zl_db[settings['set_name']]

	return zl_set


def funnel(attr, value):
	funnel = Funnel('知乎专栏关注人数漏斗图')
	funnel.add('followersCount', attr, value, is_label_show = True
			   , label_pos = "inside", label_text_color = "#fff")
	funnel.render()


if __name__ == '__main__':
	zl_set = init_mongodb()
	print(zl_set.find_one())

	# l1 = []
	# l2 = []
	# l3 = []
	# l4 = []
	# l5 = []
	# l6 = []
	# l7 = []
	# 10w +
	n1 = zl_set.find({'followersCount': {'$gte': 100000}}).count()
	print('10w+ n1 = %s' % n1)

	n2 = zl_set.find({'followersCount': {'$gte': 10000}, 'followersCount': {'$lt': 100000}}).count()
	print('1w-10w n2 = %s' % n2)

	n3 = zl_set.find({'followersCount': {'$gte': 1000}, 'followersCount': {'$lt': 10000}}).count()
	print('1k-10k n3 = %s' % n3)

	n4 = zl_set.find({'followersCount': {'$gte': 100}, 'followersCount': {'$lt': 1000}}).count()
	print('100-1000 n4 = %s' % n4)

	n5 = zl_set.find({'followersCount': {'$gte': 10}, 'followersCount': {'$lt': 100}}).count()
	print('10-100 n5 = %s' % n5)

	n6 = zl_set.find({'followersCount': {'$gte': 1}, 'followersCount': {'$lt': 10}}).count()
	print('1-10 n6 = %s' % n6)

	n7 = zl_set.find({'followersCount': 0}).count()
	print('0 n7 = %s' % n7)

	attr = ['10w+', '1w-10w', '1k-10k', '100-1000', '10-100', '1-10', '0']
	value = [n1, n2, n3, n4, n5, n6, n7]

	funnel(attr, value)
