# from threading import Thread
# import time
#
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=sayhi, args=('egon',))
#     # t.setDaemon(True)  # 必须在t.start()之前设置
#     t.start()
#
#     print('主线程')
#     print(t.is_alive())
#     '''
#     主线程
#     True
#     '''


'''
迷惑的例子

不起作用的守护线程
'''

from threading import Thread
import time


def foo():
    print(123)
    time.sleep(1)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


if __name__ == '__main__':
    t1 = Thread(target=foo)
    # t2 = Thread(target=bar)

    t1.daemon = True
    t1.start()
    # t2.start()
    print("main-------")
