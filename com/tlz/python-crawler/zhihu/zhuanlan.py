import json
import requests
from pymongo import MongoClient
import time
import threading

# header 写错了 导致一直报500错误
# header = {'UserAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'}




# 可能是反扒起作用了 加入了 Cookie 之后可以
header = {
	'Cookie':'q_c1=fe412975be0a4fa1be616f0d93622265|1516009904000|1516009904000; _zap=b6be4ccf-0bdd-4cff-aac3-820b618b3894; XSRF-TOKEN=2|a05df695|9564c0a6933ecfa18d3b93f49770c2a79138dbf4c16cc7b8c369c6a5c66d93f0976e90a5|1517661669; r_cap_id="M2I5MjNiODQ4MDQwNDYyYzhjMjgwNTViZDdlYmY5MzE=|1516071931|9bd6c1306296d5441697661db140bbf3ed9238a0"; cap_id="MTlkZjE5ZDMxMjg2NDg3N2IxN2I4YWUwYzA1YmE5Nzg=|1516071931|f8989d9a8e691ec73b83877fdbd42212669fffa7"; l_cap_id="ZGQ1NGM0MjE3YTJkNDdjMjkyYTc0MmNhYThlODE0N2U=|1516071931|ad3c804c355d26012f79f79f4eb3167edcb04040"; capsion_ticket="2|1:0|10:1516071921|14:capsion_ticket|44:YTM3ZDM3MzUwMjk5NDExYTkyNGU1MzI1YTU2NGJiMTU=|369cc6322bd5c3fb6b83c3f234e8739b445d945ebe1b5036705932fb833c623b"; z_c0=Mi4xV2gxekFnQUFBQUFBNEtIS2dXTC1EQmNBQUFCaEFsVk5DcnBLV3dCd00xQnBtUThDWnFJSVZNMVphb2Y4aldyUzRB|1516071946|bb91f11e09ceee779e3e2c4707ae835a84591cf6; _xsrf=59633c94-fea7-421e-aa11-c400f0ee73f0; aliyungf_tc=AQAAAIuIszDD5wkAiI2cc0UD8WPle/Ri; d_c0="AAAtjkNNFQ2PTjvSpXYnCPfHeZjZnba9QjY=|1517547839',
	# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'}
increment = 10

url_list = []
zl_list = []


def get_url_list():
	page = 10

	for i in range(0, increment):
		zl_url = 'https://zhuanlan.zhihu.com/api/recommendations/columns?limit=10&offset=' + str(page) + '&seed=7'
		url_list.append(zl_url)
		page += 10
	return url_list


def parse_web_info(zl_url):
	print(zl_url)
	html = requests.get(zl_url, headers = header)

	zl_json = json.loads(html.content)  # loads 不是load
	# print(zl_json)
	# break
	for zl in zl_json:
		followersCount = zl['followersCount']
		name = zl['name']
		url = 'https://zhuanlan.zhihu.com' + zl['url']
		postsCount = zl['postsCount']
		description = zl['description']
		slug = zl['slug']
		id = zl['avatar']['id']

		# 更新 逐条插入的的方式 太慢(93s) 所以：判断 如果id存在则continue (3s)

		# 这样还是有bug 通过下面这种判断 因为是列表批量插入 第一批中会出现重复 因为判断时第一批数据还没有存入数据库
		# 看来还是要唯一索引

		# if zl_set.find_one({'id': id}):
		# 	print('name = %s，id = %s 的记录已经存在，continue' % (name, id))
		# 	continue

		zl_data = {
			'followersCount': followersCount,
			'name': name,
			'url': url,
			'postsCount': postsCount,
			'description': description,
			'slug': slug,
			'id': id
		}

		# 上面的不奏效 在插入的集合中判断  列表中是否存在id  专栏id不唯一
		if zl_data in zl_list:
			print('name = %s，id = %s 的记录已经存在，continue' % (name, id))
			continue
		zl_list.append(zl_data)


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


# 重复数据
'''
(1)  唯一索引（指定字段加唯一索引）
（2） 判断 有则更新 无则插入

  (3) 数据清洗
'''


# 批量保存 会有重复的数据
def sava_data_to_mongodb(zl_list):
	# zl_set = init_mongodb()
	# print('zl_list'+str(zl_list))
	try:
		zl_set.insert_many(zl_list)
	except:
		pass


# return zl_set


# 批量保存 会有重复的数据
def sava_data_to_mongodb_plus(zl_list):
	zl_set = init_mongodb()

	for zl in zl_list:
		if zl_set.find_one({'name': zl['name']}):
			zl_set.update({'id': zl['id']},
						  {'$set': {'followersCount': zl['followersCount'], 'postsCount': zl['postsCount']}})
			print('记录已存在，更新followersCount = %s, postsCount = %s' % (zl['followersCount'], zl['postsCount']))
		else:
			zl_set.insert_one(zl)


def find_data():
	# zl_set = init_mongodb()

	# 统计满条件的结果数  算是可以迭代 但不是list 不能len()
	# mongo 有一个专门的count（）函数
	print('一共有%s条记录' % zl_set.find().count())


# for i in zl_set.find():
# 	print(i['name'])


def delete_all():
	# zl_set = init_mongodb()
	zl_set.remove()


def main_single_thread():
	start = time.time()
	url_list = get_url_list()
	for url in url_list:
		parse_web_info(url)
	sava_data_to_mongodb(zl_list)
	find_data()
	print('qTime = %s' % (time.time() - start))


# 爬虫开启多线程的的策略就是将每页的url放到一个集合里面
# 可是如果分页数太多 岂不是要爆炸？ 如何开启指定线程数？  将待启动的线程 装入到一个list

def main_multi_thread():
	start = time.time()
	url_list = get_url_list()
	threads = []
	for url in url_list:
		t = threading.Thread(target = parse_web_info, args = (url,))
		threads.append(t)
	# 	t.setDaemon(True)
	# 	t.start()
	# t.join()  # 如果不加这一句 ， zl_list为空  想想为什么？join
	# 用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

	# 开启指定线程数的
	while True:
		try:
			for i in range(0, 5):
				t = threads.pop()
				t.start()
			t.join()
			time.sleep(1)
		except:
			break
	sava_data_to_mongodb(zl_list)
	find_data()
	print('qTime = %s' % (time.time() - start))


if __name__ == '__main__':
	zl_set = init_mongodb()  # 在此声明 内部的函数可以之直接使用

	# main_single_thread()   # 单线程 存100条 qTime = 3.091722011566162
	# delete_all()
	main_multi_thread()  # 多线程 存100条 qTime = 0.8754498958587646
