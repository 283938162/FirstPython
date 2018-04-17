# coding:utf-8

import requests
from bs4 import BeautifulSoup
import time
import datetime
import itchat

header = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'
}

# 中国天气网 7天的天气信息
wealther_url = 'http://www.weather.com.cn/weather/101200101.shtml'

itchat.auto_login(hotReload = True)


def sendMsgToFriend(msg):
	friend = itchat.search_friends(u'肥宝')

	print(friend)
	userName = friend[0]['UserName']

	itchat.send(msg, toUserName = userName)


# sendMsgToFriend(u'你好')


def sendMsgToAllFriends(wea):
	friends = itchat.get_friends(update = True)
	print(friends)
	print(str(wea))


	for friend in friends:
		userName = friend['UserName']

		# send 的参数必须是字符串  []列表不行
		itchat.send(str(wea), userName)
	# print(userName)


def get_response(url):
	try:
		response = requests.get(url, headers = header)
		# return response.text    使用text 会出现中文乱码  text 字符类型 content字节类型
		return response.content
	except BaseException as e:
		print('请求网页响应失败，请检查网络', e)
		return


def get_wea_data():
	html = get_response(wealther_url)

	soup = BeautifulSoup(html, 'html.parser')

	li_all = soup.find(id = '7d').find_all('li')

	whe_3d = []

	count = 0
	for li in li_all:
		# today = time.strftime('%m-%d%',time.localtime())
		# today = datetime .date.today()+'(今日)'
		da = li.h1.text
		wea = li.find('p', class_ = 'wea').text
		tem = li.find('p', class_ = 'tem').text.replace('n', '')
		win = li.find('p', class_ = 'win').text

		# print(da, wea, tem, win)
		whe_1 = {
			'日期': da,
			'天气': wea,
			'温度': tem.replace('\n', ''),
			'风力': win.replace('\n', '')
		}

		whe_3d.append(whe_1)
		count += 1
		if count > 2:
			break

	return whe_3d
	# print(whe_3d)


# get_wea_data()

sendMsgToAllFriends(get_wea_data())
