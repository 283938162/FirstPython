# coding=utf-8

import requests
from bs4 import BeautifulSoup
import os
import sys
from multiprocessing import Pool



# version5.0 解除防盗图&模块化重构

def find_MaxPage(header):
	all_url = 'http://www.mzitu.com'
	start_html = requests.get(all_url, headers=header)
	# 寻找最大页数
	soup = BeautifulSoup(start_html.text, "html.parser")
	page = soup.find_all('a', class_='page-numbers')
	# max_page = page[-2].text

	max_page = 3  # 模拟拔取三页数据
	return max_page



def Download(href,header,title,path):
    html = requests.get(href,headers = header)
    soup = BeautifulSoup(html.text,'html.parser')
    pic_max = soup.find_all('span')
    pic_max = pic_max[10].text  # 最大页数
    if(os.path.exists(path+title.strip().replace('?','')) and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
        print('已完毕，跳过'+title)
        return 1
    print("开始扒取：" + title)
    os.makedirs(path+title.strip().replace('?',''))
    os.chdir(path + title.strip().replace('?',''))
    for num in range(1,int(pic_max)+1):
        pic = href+'/'+str(num)
        #print(pic)
        html = requests.get(pic,headers = header)
        mess = BeautifulSoup(html.text,"html.parser")
        pic_url = mess.find('img',alt = title)
        html = requests.get(pic_url['src'],headers = header)
        file_name = pic_url['src'].split(r'/')[-1]
        f = open(file_name,'wb')
        f.write(html.content)
        f.close()
    print('完成'+title)



def init():
		# 判断操作系统
	if(os.name == 'nt'):
		print(u'你正在使用win平台')
	else:
		print(u'你正在使用linux/mac平台')


	# 指定图片下载地址
	global path  #声明全局变量
	path = '/Users/anus/Documents/PythonHub/picHub/'


	# http请求头
	global all_url
	all_url = 'http://www.mzitu.com'

# 设置header,网站会根据这个判断你的浏览器以及操作系统，很多网站没有此信息将拒绝你访问（反爬虫）
# header = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}


	#http请求头
	global Hostreferer,Picreferer

	Hostreferer = {
    	'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    	'Referer':'http://www.mzitu.com'
	}
	Picreferer = {
	    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
	    'Referer':'http://i.meizitu.net'
	}
#此请求头破解盗链

def multi():
		max_page = find_MaxPage(Hostreferer)
		print(max_page)

		same_url = 'http://www.mzitu.com/page/'

		 #线程池中线程数

		pool = Pool(5)

		for n in range(1,int(max_page)+1):
				each_url = same_url+str(n)
				start_html = requests.get(each_url, headers=Hostreferer)
				soup = BeautifulSoup(start_html.text, "html.parser")
				all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
				for a in all_a:
					title = a.get_text()  # 提取文本
					if (title != ''):
						href = a['href']
						pool.apply_async(Download,args=(href,Hostreferer,title,path))
		pool.close()
		pool.join()
		print('所有图片已下完')



def main():
	init()
	multi()


if __name__ == '__main__':
	main()











# version4.0 多线程&面向对象重写（模块化）
# def find_MaxPage():
# 	all_url = 'http://www.mzitu.com'
# 	start_html = requests.get(all_url, headers=header)
# 	# 寻找最大页数
# 	soup = BeautifulSoup(start_html.text, "html.parser")
# 	page = soup.find_all('a', class_='page-numbers')
# 	# max_page = page[-2].text

# 	max_page = 10  # 模拟拔取三页数据
# 	return max_page



# def Download(href,header,title,path):
#     html = requests.get(href,headers = header)
#     soup = BeautifulSoup(html.text,'html.parser')
#     pic_max = soup.find_all('span')
#     pic_max = pic_max[10].text  # 最大页数
#     if(os.path.exists(path+title.strip().replace('?','')) and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
#         print('已完毕，跳过'+title)
#         return 1
#     print("开始扒取：" + title)
#     os.makedirs(path+title.strip().replace('?',''))
#     os.chdir(path + title.strip().replace('?',''))
#     for num in range(1,int(pic_max)+1):
#         pic = href+'/'+str(num)
#         #print(pic)
#         html = requests.get(pic,headers = header)
#         mess = BeautifulSoup(html.text,"html.parser")
#         pic_url = mess.find('img',alt = title)
#         html = requests.get(pic_url['src'],headers = header)
#         file_name = pic_url['src'].split(r'/')[-1]
#         f = open(file_name,'wb')
#         f.write(html.content)
#         f.close()
#     print('完成'+title)



# if __name__ == '__main__':
# 	# 判断操作系统
# 	if(os.name == 'nt'):
# 		print(u'你正在使用win平台')
# 	else:
# 		print(u'你正在使用linux/mac平台')


# # 指定图片下载地址
# path = '/Users/anus/Documents/PythonHub/picHub/'


# # http请求头
# all_url = 'http://www.mzitu.com'

# # 设置header,网站会根据这个判断你的浏览器以及操作系统，很多网站没有此信息将拒绝你访问（反爬虫）
# header = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

# max_page = find_MaxPage()
# print(max_page)

# same_url = 'http://www.mzitu.com/page/'


#  #线程池中线程数

# pool = Pool(5)

# for n in range(1,int(max_page)+1):
# 		each_url = same_url+str(n)
# 		start_html = requests.get(each_url, headers=header)
# 		soup = BeautifulSoup(start_html.text, "html.parser")
# 		all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
# 		for a in all_a:
# 			title = a.get_text()  # 提取文本
# 			if (title != ''):
# 				href = a['href']
# 				pool.apply_async(Download,args=(href,header,title,path))
# pool.close()
# pool.join()
# print('所有图片已下完')




# #version3.0  批量下载

# # 判断操作系统
# if(os.name == 'nt'):
# 	print(u'你正在使用win平台')
# else:
# 	print(u'你正在使用linux/mac平台')


# # 指定图片下载地址
# path = '/Users/anus/Documents/PythonHub/picHub'


# # http请求头
# all_url = 'http://www.mzitu.com'

# # 设置header,网站会根据这个判断你的浏览器以及操作系统，很多网站没有此信息将拒绝你访问（反爬虫）
# header = {
#	 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}


# # 用get方法打开url并发送header（向目的网站发起请求信息，html为网站应答）
# start_html = requests.get(all_url, headers=header)


# # 打印结果 .text是返回的结果打印出文本格式
# # print(html.text)

# # 使用自带的html.parser解析,通用型强 但是速度慢, 结果返回一个soup对象
# soup = BeautifulSoup(start_html.text, 'html.parser')

# # 寻找最大页数
# page = soup.find_all('a', class_='page-numbers')

# # print(page)

# print(page[-2].text)

# # max_page = page[-2].text

# # 模拟最大页码 2

# max_page = 2


# same_url = 'http://www.mzitu.com/page/'

# for n in range(1, int(max_page) + 1):
# 	page_url = same_url + str(n)
# 	start_html = requests.get(page_url, headers=header)
# 	soup = BeautifulSoup(start_html.text, 'html.parser')

# 	all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
# 	for a in all_a:
# 		title = a.get_text()  # 提取文本
# 		if(title != ''):
# 			print("准备扒取：",title)

# 			# win不能创建带？的目录
# 			if(os.path.exists(path+title.strip().replace('?',''))):
# 				flag = 1; #目录已经存在
# 			else:
# 				os.makedirs(path+title.strip().replace('?',''))
# 				flag = 0


# 			os.chdir(path + title.strip().replace('?', ''))

# 			href = a['href']
# 			html = requests.get(href, headers=header)
# 			mess = BeautifulSoup(html.text, "html.parser")
# 			pic_max = mess.find_all('span')
# 			pic_max = pic_max[10].text  # 最大页数
# 			if(flag == 1 and len(os.listdir(path + title.strip().replace('?', ''))) >= int(pic_max)):
# 				print('已经保存完毕，跳过')
# 				continue
# 			for num in range(1, int(pic_max) + 1):
# 				pic = href + '/' + str(num)
# 				html = requests.get(pic, headers=header)
# 				mess = BeautifulSoup(html.text, "html.parser")
# 				pic_url = mess.find('img', alt=title)
# 				html = requests.get(pic_url['src'], headers=header)
# 				file_name = pic_url['src'].split(r'/')[-1]

# 				f = open(file_name, 'wb')
# 				f.write(html.content)
# 				f.close()
# 			print('完成')
# 	print('第',n,'页完成')


# version 单页 获取图片单个套图

# #最大页数在span标签中的第10个
# pic_max = soup.find_all('span')[10].text

# print('图片数量：',pic_max)


# title = soup.find('h2',class_='main-title').text
# print('图片标题：',title)


# #输出每个图片的页面地址
# for i in range(1,int(pic_max) + 1):
# 	href = url + '/' +str(i)

# 	print('图片链接：',href)
# 	html = requests.get(href,headers = header)
# 	mess = BeautifulSoup(html.text,'html.parser')

# 	# print(html.text)
# 	#图片地址在img标签alt属性和标题一样的地方
# 	pic_url = mess.find('img',alt = title)
# 	print('图片地址：',pic_url['src'])

# 	html = requests.get(pic_url['src'],headers=header)

# 	#获取图片的名字方便命名
# 	file_name = pic_url['src'].split(r'/')[-1]

# 	print('file_name =',file_name)

# 	#图片不是文本文件，以二进制格式写入，所以是html.content

# 	#如果不指定路径的话 默认下载路径是脚本当前路径
# 	f = open(file_name,'wb')
# 	f.write(html.content)
# 	f.close


# version1.0  测试soup

# # #实际上是第一个class=‘postlist’的div里的所有a标签是我们要找的信息
# # all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')

# # # all_a = soup.find('div',class_='postlist').find_all('span','target')


# # for a in all_a:
# # 	title = a.text# 提取文本
# # 	# print (title)
