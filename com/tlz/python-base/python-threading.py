# conding:utf-8

import threading
from time import ctime, sleep

'''
deamon 守护线程不起作用

'''


# def music(func):
#     for i in range(2):
#         print('a to %s. %s. %s' % (func, ctime(), threading.current_thread().name))
#         sleep(1)
#
#
# def move(func):
#     for i in range(3):
#         print('b to %s. %s. %s' % (func, ctime(), threading.current_thread().name))
#         sleep(2)


# threads = []
# t1 = threading.Thread(target=music, args=('A',))
# threads.append(t1)
#
# t2 =
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         # t.setDaemon(True)
#         t.start()
#     # 方法，用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
#     t.join()
#     print('all to %s. %s' % (ctime(), threading.current_thread().name))


# 2.通过继承 thread.Thread 类 来创建线程
# 这种方法只需要重载 threading.Thread 类的 run 方法，然后调用 start()开启线程就可以了
class mythread(threading.Thread):
    def run(self):
        global x
        # lock.acquire()  # 放在lock 原子操作
        x+=10
        print('%s:%d'%(self.name,x))
        # lock.release()
x = 0
lock = threading.RLock() # 创建 可重入所

def main():
    l = []
    for i in range(10):
        l.append(mythread())  # 创建一个线程组 放入5条线程
    for i in l:
        i.start()

if __name__ == '__main__':
    main()






# def main():
#     # mythread().setDaemon(True)
#     # mythread().start()
#
#     t = mythread()
#     # 感觉这守护线程 不对劲啊
#     t.daemon = True
#     t.start()
#
#     print("main thread over!")
#
#
# if __name__ == '__main__':
#     main()

'''
加入 t.join() 之后 AB模块几乎同时被启动 muti线程

a to A. Sat Jan 20 18:13:32 2018. Thread-1
b to B. Sat Jan 20 18:13:32 2018. Thread-2
a to A. Sat Jan 20 18:13:33 2018. Thread-1
b to B. Sat Jan 20 18:13:34 2018. Thread-2
b to B. Sat Jan 20 18:13:36 2018. Thread-2
all to Sat Jan 20 18:13:38 2018. MainThread
'''
