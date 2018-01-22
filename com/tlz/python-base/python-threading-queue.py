import queue
import time
import subprocess
import threading

q = queue.Queue()

hosts = ['192.168.1.68', '192.168.1.118', '192.168.1.101', '192.168.1.250', '192.168.1.133']


def run():
    # while true 防止线程少于len(hosts)时卡死，不用while循环线程数少时就会导致队列数据无法全部取完，就会造成queue.join()一直阻塞状态
    while True:
        host = q.get()
        print('host ip is:%s' % host)
        # print(q.qsize())
        # if host == '192.168.1.118':
        #     time.sleep(10)
        # print('host ip is:%s' % host)
        # q.task_done()  # 当前线程任务完成


def main():
    for i in range(10):
        t = threading.Thread(target=run)
        t.setDaemon(True)
        t.start()

    for i in hosts:
        q.put(i)

    q.join()  # 阻塞直到所有的线程queue.task_done()


if __name__ == '__main__':
    start = time.time()
    main()
    print("Elapsed Time: %s" % (time.time() - start))
