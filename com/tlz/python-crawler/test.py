# -*- coding:utf-8 -*-

#使用正则表达式抓取，不适用
import requests
import re
from bs4 import BeautifulSoup

 
# head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# TimeOut = 30


 
# def requestpageText(url):
#       try:
#           Page = requests.session().get(url,headers=head,timeout=TimeOut)
#           Page.encoding = "gb2312"
#           return Page.text
#       except BaseException as e:
#           print("联网失败了...",e)
 
# site = "http://huaban.com/favorite/beauty/"
# text = requestpageText(site)#抓取网页源码
# print(text)


# beautifulsoup版
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 30

site = "https://8xdn.com/"

 
def requestpageText(url):
    try:
        Page = requests.session().get(url,headers=head,timeout=TimeOut)
        Page.encoding = "utf-8"
        return Page.text
    except BaseException as e:
        print("联网失败了...",e)
 
text = requestpageText(site)#抓取网页源码

soup = BeautifulSoup(text,'html.parser')
# print(soup)

data = soup.find_all('div',class_="image-container")

# print(data)

for x in data:
    # print(x)
    a_all = x.find_all('a')

    if a_all[0].find('img',width='342') is None:
        continue
    print(a_all[0].find('img',width='342'))
    # print(a_all[1].text)



# # 正则写法
# import re
# import os
# import requests
# import time

# # 全局变量
# global PhotoNum
# PhotoNum = 0
# PWD = "/Users/anus/Documents/PythonHub/picHub/"
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# TimeOut = 30

# url = "http://huaban.com/favorite/beauty/"
# url_image = "http://hbimg.b0.upaiyun.com/"
# urlNext = "http://huaban.com/favorite/beauty/?iqkxaeyv&limit=20&wfl=1&max="


# def downfile(file, url):
#     print("开始下载：", file, url)
#     try:
#         r = requests.get(url, stream=True)
#         with open(file, 'wb') as fd:
#             for chunk in r.iter_content():
#                 fd.write(chunk)
#     except Exception as e:
#         print("下载失败了", e)


# def requestpageText(url):
#     try:
#         Page = requests.session().get(url, headers=head, timeout=TimeOut)
#         Page.encoding = "utf-8"
#         return Page.text
#     except Exception as e:
#         print("联网失败了...重试中", e)
#         time.sleep(5)
#         print("暂停结束")
#         requestpageText(url)


# def requestUrl(url):
#     global PhotoNum
#     print("*******************************************************************")
#     print("请求网址：", url)
#     text = requestpageText(url)
#     pattern = re.compile(
#         '{"pin_id":(\d*?),.*?"key":"(.*?)",.*?"like_count":(\d*?),.*?"repin_count":(\d*?),.*?}', re.S)
#     items = re.findall(pattern, text)
#     print(items)
#     max_pin_id = 0
#     for item in items:
#         max_pin_id = item[0]
#         x_key = item[1]
#         x_like_count = int(item[2])
#         x_repin_count = int(item[3])
#         if (x_repin_count > 10 and x_like_count > 10) or x_repin_count > 100 or x_like_count > 20:
#             print("开始下载第{0}张图片".format(PhotoNum))
#             url_item = url_image + x_key
#             filename = PWD + str(max_pin_id) + ".jpg"
#             if os.path.isfile(filename):
#                 print("文件存在：", filename)
#                 continue

#             downfile(filename, url_item)
#             PhotoNum += 1
#     requestUrl(urlNext + max_pin_id)


# # 程序入口 主函数
# if not os.path.exists(PWD):
#     os.makedirs(PWD)
# requestUrl(url)



