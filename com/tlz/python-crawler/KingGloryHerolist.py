from urllib import parse

import requests
import json
import sys
import os
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
import time

'''
不要被套路限制了思想

'''

url = 'https://pvp.qq.com/web201605/herolist.shtml'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0'}
herolist_json = 'https://pvp.qq.com/web201605/js/herolist.json'
saveFolder = 'image'


def get_hero_list():
    # hero_json = requests.get(herolist_json).text
    # hero_info = json.loads(hero_json)

    # 等价于上面两句 如果解析的已知json，可以直接 requests.get().json(
    hero_info = requests.get(herolist_json).json()
    return hero_info


def get_skin():
    hero_list = get_hero_list()
    for i in hero_list:
        ename = i['ename']
        cname = i['cname']
        skin_name = i['skin_name']
        makedir(saveFolder)

        print(ename, cname, skin_name)

        title_all = skin_name.split('|')

        for i in range(1, len(title_all) + 1):
            pic_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(ename,
                                                                                                               ename, i)
            print(pic_url)

            # FileNotFoundError: [Errno 2] No such file or directory: '/Users/anus/PycharmProjects/FirstPython/com/tlz/python-crawler/image/廉颇/正义爆轰.jpg'

            makedir(saveFolder, cname)  # 如果没这句 会出现上面的错误 因为 os不能创建多级文件夹

            pic_path = os.path.join(sys.path[0], saveFolder, cname, title_all[i - 1] + '.jpg')

            if download_img(pic_url, pic_path):
                print('正在下载图片,{}_{}'.format(cname, title_all[i - 1]))


def download_img(url, path):
    try:
        image_data = requests.get(url, timeout=15)
    except BaseException as e:
        print('下载图片出错,%s,%s' % (e, url))
        return False
    with open(path, 'wb') as f:
        f.write(image_data.content)
    return True


# 构建路径 如果路径重复就合并呗！
def makedir(*dirname):
    dirpath = os.path.join(sys.path[0], *dirname)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)


# 页面采用异步加载 get到的东西  跟查看器中的内容 源码中内容不一致且被注释掉
def get_herolist_by_bs4():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')

    ul_all = soup.find_all('ul', class_='herolist clearfix')

    print(ul_all)


def get_herolist_by_bs4_selenium():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(3)

    html = driver.page_source

    # print(html)   # 这个网页才出现了我们需要的内容

    # 对网页解析（1）bs （2）selenium

    # 方法一：bs
    get_element_by_bs(html)

    # 方法二：selenium
    # get_element_by_selenuim(driver)


def get_element_by_bs(html):
    soup = BeautifulSoup(html,
                         'html.parser')  # 传入的html本身已经是str 不需要 html.text 否则AttributeError: 'str' object has no attribute 'text'

    li_all = soup.find('ul', class_='herolist clearfix').find_all('li')

    # print(ul_all)
    ori_url = 'https://pvp.qq.com/web201605/'
    for li in li_all:
        hero_url = ori_url + li.a['href']
        print(hero_url)

        hero_name = li.text
        print(hero_name)


def get_element_by_selenuim(driver):
    # 使用xpath
    li_all = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/ul/li')
    # 使用类选择器 class中出现空格的地方 换成点  开头也要加点
    # li_all = driver.find_element_by_css_selector('.herolist.clearfix').find_elements_by_tag_name('li')

    # li_all = driver.find_elements_by_tag_name('img')
    # print(len(li_all))
    # print(li_all)

    '''
    好像标签才有 get_attribute('属性')的方法  
    WebElement 也都有text属性 类似bs
    
    css_seceltor 还有driver.find_element_by_css_selector（'标签[属性]'） 进行精准匹配
    '''

    for li in li_all:
        # hero_url = li.find_element_by_tag_name('a').get_attribute('href')  # 获取 该标签下执行属性的值
        # print(hero_url)

        # hero_name = li.find_element_by_tag_name('img').get_attribute('alt')
        hero_name = li.find_element_by_tag_name('a').text

        print(hero_name)

    driver.close()


if __name__ == '__main__':
    get_skin()
    # get_herolist_by_bs4()
    # get_herolist_by_bs4_selenium()
