import pdfkit

'''
pdfkit，把HTML+CSS格式的文件转换成PDF格式文档的一种工具。

其实，它就是html转成pdf工具包wkhtmltopdf的Python封装。

所以，必须安装wkhtmltopdf。 一般情况下，wkhtmltopdf需要手动安装，尤其要注意的是Windows下，需要把wkhtmltopdf的bin执行文件路径添加到PATH变量中。
'''
#
# output_url = 'http://blog.csdn.net/shenwanjiang111/article/details/68925569'
# output_file = 'Python工具-pdfkit - CSDN博客.html'
# output_string = '测试'
#
# pdfkit.from_url(output_url, 'out1.pdf')
# pdfkit.from_file(output_file, 'out2.pdf')
# pdfkit.from_string(output_string, 'out3.pdf')

import requests
from bs4 import BeautifulSoup
import pdfkit
import os

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000'

header = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'
}


options = {
	'page-size': 'Letter',
	'margin-top': '0.75in',
	'margin-right': '0.75in',
	'margin-bottom': '0.75in',
	'margin-left': '0.75in',
	'encoding': "UTF-8",
	'custom-header': [
		('Accept-Encoding', 'gzip')
	],
	'cookie': [
		('cookie-name1', 'cookie-value1'),
		('cookie-name2', 'cookie-value2'),
	],
	'outline-depth': 10,
}

def get_html_text():
	try:
		html = requests.get(url, headers = header)
	except BaseException as e:
		print('获取原网页失败！', e)
	return html.content


html = get_html_text()
soup = BeautifulSoup(html, 'html.parser')

# print(soup.text)
# soup select
# article = soup.select('.article.article_16')[0]   #通过类名查找 类名前加 点 .
article = soup.select('.x-wiki-content.x-main-content')[0]  # 通过id查找 id前加井号 #

print(type(article))
article = str(article)
print(type(article))

html = html_template.format(content = article)
html = html.encode('utf-8')

with open('py.html', 'wb') as f:
	f.write(html)

# 将需要的网页保存下来 然后在保存成html
pdfkit.from_file('py.html', 'py.pdf',options = options)

# 删除临时保存下来的 切割后的网页
os.remove('py.html')
print('succeed')
