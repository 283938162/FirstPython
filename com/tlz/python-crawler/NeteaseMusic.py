import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import re

# mid = 2116  # 音乐人id
# murl = 'http://music.163.com/#/artist?id=' + str(mid)
#
# sid = 5255662  # 歌曲id
# surl = 'http://music.163.com/#/song?id=' + str(sid)
#
# # lurl = 'http://music.163.com/api/song/lyric?' + 'id=' + str(sid) + '&lv=1&kv=1&tv=-1'  # 歌词url
#
# 模拟浏览器登录
header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}#


playlist_url = 'http://music.163.com/#/playlist?id=317113395'
artist_url = 'http://music.163.com/artist?id=2116'

def get_song_ids():
    # executable_path 为你安装phantomJS的可执行的文件路径
    driver = webdriver.PhantomJS(executable_path='/Users/anus/local/phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.maximize_window()  # 设置全屏

    url = artist_url
    driver.get(url)  # 执行js

    # 网易云采取了框架，所以必须要加上这一句，就可以返回框架的源代码了
    driver.switch_to.frame(driver.find_element_by_name("contentFrame"))

    html = driver.page_source  # 将浏览器执行后的源代码付给html

    soup = BeautifulSoup(html, 'html.parser')

    # print(soup)

    span_all = soup.find_all('span', 'txt')
    nums = len(span_all)

    if url != artist_url:
        songs_name = soup.find('h2',class_="f-ff2 f-brk")
        print('******歌单: '+songs_name.text+' 共 '+str(nums)+' 首歌*****\n')

    # print(span_all)

    for hf in span_all:
        a = hf.a['href']
        # print(a)
        # id = re.findall(r'\d+',a) # python 正则的用法  结果['41500032']

        id = re.findall(r'\d+', a)[0]  # python 正则的用法
        title = hf.b['title']
        print(id,title)

        # 打印并保存

        # print('*****start*****\n')
        # print('歌名：'+title+'\n')
        #
        # lyric = get_song_lyric(id)
        # print('*****end*****\n')
        #
        # # 保存
        # save('ts.txt',lyric)



def get_song_lyric(sid):

    lurl = 'http://music.163.com/api/song/lyric?' + 'id=' + str(sid) + '&lv=1&kv=1&tv=-1'  # 歌词url

    html = requests.get(url=lurl, headers=header)
    json_python = json.loads(html.text)
    # print()

    ly = json_python['lrc']['lyric']
    pat = re.compile(r'\[.*\]')
    lrc = re.sub(pat,"",ly)
    print(lrc.strip())

    return lrc.strip()

def save(filename,contents):
    # f = open(filename,'w+')
    # f.write(contents)
    # f.close()

    with open(filename,'a',encoding='utf-8') as f:
        f.write(contents)

    print('文件写入成功')

if __name__ == '__main__':
    # get_song_lyric(sid)
    get_song_ids()






# print(soup.title)
#
# print(soup.a) #查找第一个指定标签  可以使用find_all查找全部
#
# print(soup.find_all('a').__len__()) # 集合长度的另一种输出方法


# m_top = soup.find('div',class_='m-top')

# print(m_top)

# 对标签的直接子节点进行循环
# 注意循环的事直接子节点（标签+内容）
# title_tag = soup.li
# for child in title_tag.children:
#     print(child)
#
# soup.parent #父节点
#
# # 所有父节点
# link = soup.a
# for parent in link.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
