# encoding=utf-8
'''

Mongo Conn连接类
'''

import pymongo


class DBConn:
    conn = None
    servers = "mongodb://39.108.231.238:27017"

    def connect(self):
        self.conn = pymongo.Connection(self.servers)

    def close(self):
        return self.conn.disconnect()

    def getConn(self):
        return self.conn

if __name__ == '__main__':
    print(DBConn.connect())
