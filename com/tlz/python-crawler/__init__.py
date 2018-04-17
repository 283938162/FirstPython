import requests
import json

start_url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"

header = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'
}

def get_html_text():
	try:
		html = requests.get(start_url,headers=header)
	except BaseException as e:
		print('获取原网页失败！',e)
	return html.text

print(get_html_text())