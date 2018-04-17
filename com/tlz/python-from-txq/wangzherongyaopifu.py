# coding:utf-8
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import urllib.request

url = 'https://pvp.qq.com/web201605/herolist.shtml'

save_dir = 'F:\heroskin\\'  # 文件夹不存在则创建
if not os.path.exists(save_dir):
    os.mkdir(save_dir)


driver=webdriver.Chrome()
def get_all_hero_ids(url):
    # driver = webdriver.PhantomJS(
    #     executable_path=r'D:\WorkSpace\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url)
    # print(driver.page_source)
    hero_ids = driver.find_element_by_class_name("herolist-content").find_elements_by_tag_name('a')

    for i in hero_ids:
        ids = i.get_attribute('href')
        # print(ids)
        names = i.text
        # print(names)
        # return ids,names
        ##得到所有英雄的网址

        get_hero_all_skins(names, ids)


def get_hero_all_skins(name, id):
    # driver=webdriver.Firefox()
    # driver = webdriver.PhantomJS(
    #     executable_path=r'D:\WorkSpace\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(id)
    # print(driver.page_source)
    skins_ = driver.find_element_by_class_name("pic-pf")
    skins = skins_.find_elements_by_tag_name('img')
    for i in skins:
        hero_skins = i.get_attribute('data-imgname')
        hero_skins_name = i.get_attribute('data-title')

        # 创建路径，如果路径存在就合并，不然会报错
        hero_dir = os.path.join('F:\heroskin' + '\\' + name)
        if not os.path.exists(hero_dir):
            os.makedirs(hero_dir)
        urllib.request.urlretrieve('http:' + hero_skins.strip(), hero_dir + '\\' + hero_skins_name + '.jpg')

        # return hero_skins,hero_skins_name
        ##得到英雄的皮肤和皮肤对应的名字


if __name__ == '__main__':
    # get_hero_all_skins('明世隐','https://pvp.qq.com/web201605/herodetail/501.shtml')
    get_all_hero_ids(url)
