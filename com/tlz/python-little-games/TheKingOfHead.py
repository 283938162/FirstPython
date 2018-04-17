# coding:utf-8

'''
头脑王者
今天用Python编写一个脚本，调用百度API，进行自动检索答题，自动识别出现频率最多的答案，然后列出并选择。


需要百度的aip模块
https://github.com/Baidu-AIP/python-sdk



c参考：
https://github.com/zhuweiyou/weixin-game-helper/tree/master/%E5%A4%B4%E8%84%91%E7%8E%8B%E8%80%85

'''

import os
import random
import requests
import subprocess
import time

from PIL.Image import frombytes
from aip import AipOcr
from io import BytesIO
from PIL import Image


def run():
	# print('准备答题了！')
	while True:
		# input('输入回车开始答题：')
		img = get_screenshot()
		info = get_word_by_img(img.getvalue())

		# 至少是5个words
		if info['words_result_num'] < 5:
			continue

		# print(info['words_result'])
		# print(info['words_result'][-4:])

		#  这是什么写法？
		anwsers = [x['words'] for x in info['words_result'][-4:]]

		question = [x['words'] for x in info['words_result'][-6:-4]]

		# question = ''.join(anwser)
		question = ''.join(question)
		# anwsers = ''.join(anwsers)

		print('question=%s' % question)
		print('answers=%s' % anwsers)

		res = baidu(question, anwsers)
		print(res)

		print('这道题的答案是 {}'.format(res[0][1]))
		break
		# print(config['头脑王者']['point'][res[0][2]])
		# click(config['头脑王者']['point'][res[0][2]])


def baidu(question, anwsers):
	url = 'https://www.baidu.com/s'
	header = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'
	}
	data = {
		'wd': question
	}

	res = requests.get(url, params = data, headers = header)
	res.encoding = 'utf-8'
	html = res.text

	# print(html)

	# i 答案出现的次序
	for i in range(len(anwsers)):
		# 这个count 不是精准匹配 比如 石公 黄石公也匹配到了  中文分词问题吗
		anwsers[i] = (html.count(anwsers[i]), anwsers[i], i)

	# [(0, '青石公', 0), (0, '白石公', 1), (9, '石公', 2), (9, '黄石公', 3)]

	# print(anwsers)

	#  按list的哪个字段排序？
	anwsers.sort(reverse = True)
	# print('late=%s' % anwsers)
	return anwsers


'''
这个api有个问题 就是 如果换行 自动识别为一个words 
后面ABCD 是个答案 所以之前的words要合并成一句话！

{
    'log_id': 6987985864026954702, 
    'words_result_num': 6, 
    'words_result': [
        {'words': '「张良拾履」典故中,赠与张良兵'}, 
        {'words': '书的老人是?'}, 
        {'words': '青石公'}, 
        {'words': '白石公'}, 
        {'words': '石公'}, 
        {'words': '黄石公'}
        ]
}

'''


def get_word_by_img(img):
	APP_ID = '10737197'
	API_KEY = 'F1ufDLiN9jKMsUdnhhkGOs5O'
	Secret_KEY = 'wFDZ3q3a06WOWeV3gzQO9mEEdMeLbdz7'

	client = AipOcr(APP_ID, API_KEY, Secret_KEY)

	print(img)
	res = client.basicGeneral(img)
	# print('识图内容：%s\n' % res)

	return res


config = {
	'头脑王者': (76, 355, 465, 390),
	'answers': (76, 460, 465, 870),
	'point': [
		(76, 470, 465, 560),
		(76, 580, 465, 660),
		(76, 670, 465, 755),
		(76, 765, 465, 850),
	]
}


def get_screenshot():
	img = Image.open('wz2.jpg')

	width = img.size[0]
	height = img.size[1]

	# print('原图宽=%s，高=%s' % (width, height))

	# box=(x0,y0,x1,y1)  截图框的对接线两点的左边
	# 左上角和右下角的像素点  参数必须是四元组
	title_img = img.crop((80, 500, 1050, 876))  # 标题
	answer_img = img.crop((180, 915, 915, 1735))  # 答案

	# title_img.show()
	# answer_img.show()

	#  size A 2-tuple, containing (width, height) in pixels.
	new_img = Image.new("RGBA", (width, 1300))  # 新建一块空白版

	# size A 2-tuple or A 4-tuple

	new_img.paste(title_img, (0, 0))
	# new_img.paste(answer_img, (0, 370))
	new_img.paste(answer_img, (0, 450))

	# new_img.show()

	new_img_fb = BytesIO()
	new_img.save(new_img_fb, 'png')

	return new_img_fb


def pic_ocr():
	# 读取图片 返回一个Image对象
	img = Image.open('wz.jpg')
	print(img.format)

	# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO
	img_fb = BytesIO()
	# print(img_fb)
	# print(img_fb.getvalue())

	'''
	 You can use a file object instead of a filename. In this case,
		you must always specify the format. The file object must
		implement the ``seek``, ``tell``, and ``write``
		methods, and be opened in binary mode.
		:param fp: A filename (string), pathlib.Path object or file object.
	'''
	# print('***before***')
	# 用户可以使用文件对象代替文件名称。在这种情况下，用户必须指定文件格式。
	# 文件对象必须实现了seek()、tell()和write()方法，且其以二进制模式打开。
	# 原来玄机在这里 将图片信息转换二进制信息保存到img_fb  必须指定图片格式 支持png/jpeg  注：jpg是jpeg的一种格式
	img.save(img_fb, 'jpeg')
	# print('***after***')

	# print(img.format)
	# print(img_fb)
	# print(img_fb.getvalue())

	# 调用百度借口ocr
	res = get_word_by_img(img_fb.getvalue())
	return res


if __name__ == '__main__':
	# get_screenshot()
	# print(img_fb)

	# img = get_screenshot()
	# res = get_word_by_img(img.getvalue())
	# print(res)

	# start = time.time()
	# run()
	# print('qTime=%s' % (time.time() - start))

	# img_byte = BytesIO()
	# res =
	# print(res)

	print(pic_ocr())

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

# fb = BytesIO(b'zdf')
# print(fb.getvalue())
