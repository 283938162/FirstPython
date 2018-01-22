# coding:utf-8

# 将从网页抓取的内容存入数据库
import requests

import requests
from bs4 import BeautifulSoup

import pymysql

header = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
url = "http://html-color-codes.info/color-names/"

hostname = '39.108.231.238'
username = 'aliyun'
password = 'Ali1819!@'
dbname = 'TESTDB'


def initdb():
    global db
    db = pymysql.connect(hostname, username, password, dbname)
    createdb(db)


def createdb(db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS COLOR")
    sql = """CREATE TABLE COLOR (
        ID INT(4) PRIMARY KEY not NULL auto_increment,
        Color CHAR(20) NOT NULL,
        Value CHAR(10),
        Style CHAR(50) )"""

    cursor.execute(sql)


def insertdb(db, style, color, value):
    cursor = db.cursor()
    sql = "insert into COLOR VALUES (NULL,'" + color + "','" + value + "','" + style + "')"
    try:
        cursor.execute(sql)
        db.commit()
        print("插入成功！color:%s,value:%s,style:%s" % (color, value, style))
    except BaseException as e:
        print("插入失败!", e)  # 打印异常
        db.rollback()


def closedb(db):
    db.close()


def save_web_data(style, color, value):
    insertdb(db, style, color, value)
    # closedb(db)  # 为啥插入的数据只有一行呢？ 数据库关闭的位置？


def get_web_data():
    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    all_color = soup.find_all('table', class_='colortable')

    # print(all_color)

    # all_color = soup.find_all('h2')
    for x in all_color:
        all_tr = x.find_all('tr')
        # print(all_tr)
        for x in all_tr:
            style = x['style']
            # print(style)
            color = x.find_all('td')[1].text
            value = x.find_all('td')[2].text

            save_web_data(style, color, value)

    closedb(db)  # 设db为全局变量才可以在函数内部使用其他函数内部的变量


def main():
    initdb()
    get_web_data()


if __name__ == '__main__':
    main()
