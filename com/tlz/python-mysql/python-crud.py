# coding=utf-8
import pymysql

hostname = '39.108.231.238'
username = 'aliyun'
password = 'Ali1819!@'
dbname = 'TESTDB'


def connectdb():
    print('连接mysql服务器...')

    # 打开数据库，获取连接

    db = pymysql.connect(hostname, username, password, dbname)

    print('连接上了！')
    return db


def createtable(db):
    # 使用cursor（）方法获取操作游标
    cursor = db.cursor()

    # 如果存在Student先删除
    cursor.execute("drop table if EXISTS student")

    sql = """create table student(
              ID char(10) not NULL,
              Name char(8),
              Grade INT )"""
    # 执行sql 创建student
    cursor.execute(sql)


def insertdb(db):
    # 使用cursor（）方法获取操作鼠标
    cursor = db.cursor()

    # SQL 插入数据
    sql = """insert into student 
              VALUES  ('001','czq',70),
                      ('002','lhq',80),
                      ('003','czq',70),
                      ('004','lhq',80),
                      ('005','czq',70),
                      ('007','lhq',80)"""

    try:
        # 执行sql语句,执行插入操作
        cursor.execute(sql)
        db.commit()
        print('插入数据成功')
    except:
        # Rollback in case there is any error
        print('插入数据失败')
        db.rollback()


def querydb(db):
    # 使用cursor（）方法获取操作鼠标
    cursor = db.cursor()

    # 查询sql

    sql = "SELECT * FROM student WHERE grade >= '%d'" % (80)


    try:
        # 执行sql
        cursor.execute(sql)

        # 获取所有记录列表
        results = cursor.fetchall()

        print(results)

        # 遍历结果集
        for row in results:
            ID = row[0]
            Name = row[1]
            Grade = row[2]

            # 打印结果
            print("ID: %s, Name: %s, Grade: %d" %(ID, Name, Grade))  # python3 的格式化输出
    except:
        print('Error: unable to fetch data')


def deletedb(db):
    cursor = db.cursor()

    sql = "delete from student where id = '%s'"%('001')

    try:
        cursor.execute(sql)
        db.commit()
        print("删除成功")
    except:
        print("删除失败")
        db.rollback()


def updatedb(db):
    cursor = db.cursor()
    sql = "update student set grade='%d'"%(90) + "where id = '%s'"%('002')
    try:
        cursor.execute(sql)
        db.commit()
        print("更新成功")
    except:
        print("更新失败")
        db.rollback()


def closedb(db):
    db.close()


def main():
    db = connectdb()  # 连接mysql数据库
    print(db)

    # createtable(db)  # 创建表
    #
    # insertdb(db)  # 插入数据

    # querydb(db)  # 查询数据库

    # deletedb(db) # 删除数据

    updatedb(db) # 更新数据

    closedb(db) # 关闭数据库


if __name__ == '__main__':
    main()
