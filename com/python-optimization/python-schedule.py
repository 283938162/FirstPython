import schedule
import time

'''

schedule 是一个第三方的 定时任务模块

'''


def task():
    print('i am wordking ...')


if __name__ == '__main__':

    # 每秒执行一次任务  以秒为单位  second 单数 every() 不传参数 do 函数名称（类似多线程）
    schedule.every().second.do(task)

    # 每3s执行一次任务 second 要用复数seconds
    # schedule.every(3).seconds.do(task)

    # schedule.every(10).minutes.do(job)  #  每十分钟执行一次
    # schedule.every().hour.do(job) #每个小时执行一次
    # schedule.every().day.at("10:30").do(job) # 每天10：30执行一次  注意at 参数是次级时间参数）
    # schedule.every().monday.do(job)  # 每个月
    # schedule.every().wednesday.at("13:15").do(job) 每周四13：15执行一次

    while True:
        schedule.run_pending()
        time.sleep(1)
