# coding=utf-8

# 扒取www.shaoit.com
# 标题 Title 时间 AddOn 分类 Category  浏览量 Views  简介 Description


import requests
from bs4 import BeautifulSoup

import pymysql

header = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
url = "http://www.shaoit.com/page/1"

hostname = '39.108.231.238'
username = 'aliyun'
password = 'Ali1819!@'
dbname = 'TESTDB'


def init_db():
    global db
    db = pymysql.connect(hostname, username, password, dbname,charset="utf8")
    create_table(db)


def create_table(db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS SHAOIT")
    sql = """CREATE TABLE SHAOIT (
        ID INT(4) PRIMARY KEY NOT NULL AUTO_INCREMENT,
        Title VARCHAR (255) NOT NULL,
        AddOn VARCHAR (100),
        Category VARCHAR (100),
        Views VARCHAR (255),
        Description TEXT)"""

    # 捕获并打印异常
    try:
        cursor.execute(sql)
        db.commit()
        print('建表成功!')
    except BaseException as e:
        print('建表失败!', e)


def save_web_data(title, addon, category, views, description):
    cursor = db.cursor()
    sql = "INSERT INTO SHAOIT VALUES (NULL,'" + title + "','" + addon + "','" + category + "','" + views + "','" + description + "')"
    try:
        cursor.execute(sql)
        db.commit()
        print("插入成功！\n title:%s\n,addon:%s\n,category:%s\n,views:%s\n,description:%s" % (title, addon,category, views, description))
        print('***********插入一条数据***********')
    except BaseException as e:
        print("插入失败!", e)  # 打印异常
        db.rollback()


def get_web_data():
    try:
        html = requests.get(url, headers=header)
        soup = BeautifulSoup(html.text, 'html.parser')
        # print(soup)
    except BaseException as e:
        print("请求失败", e)

    all_data = soup.find_all('div', class_='box_entry')
    for x in all_data:
        title = x.h2.a.text;  # 标签之间可以直接点号引用
        addon = x.find('span', class_='date').text
        category = x.find('span', class_='category').a.text  # x.find 相当于一个soup对象 对象可以直接引用标签 也可以find
        # views = x.find('div',class_='info').text
        #
        # views.replace('阅读','yuedu')

        views = '234,45'

        description = x.find('div', class_='post_entry').text.strip()

        save_web_data(title, addon, category, views, description)
    # db.close()

if __name__ == '__main__':
    init_db()
    get_web_data()
