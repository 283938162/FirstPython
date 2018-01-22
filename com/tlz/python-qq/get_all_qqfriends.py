# coding:utf-8
from selenium import webdriver
import time, os
import xlrd, xlwt
from xlutils.copy import copy
import re

'''
爬取并存入excel

未抓取 设备名称，评论内容

'''

# 使用selenium
# 使用selenium的隐藏PhantimJS浏览器登陆账号后对内容获取
# 注意frame与iframe的格式框切换
# driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver = webdriver.Chrome()
# driver.set_preference('network.proxy.type', 1)
# driver.set_preference('network.proxy.http', '127.0.0.1')
# driver.set_preference('network.proxy.http_port', 17890)
driver.maximize_window()

username = ''
password = ''

work_path = '/Users/anus/PycharmProjects/FirstPython/com/tlz/python-qq/data/qq.xls'
qq_love_index_path = '/Users/anus/PycharmProjects/FirstPython/com/tlz/python-qq/data/qq_love_index.xls'
values = []

# 加头
value_head = ['qq号码', 'qq昵称', '发表时间', '点赞数', '评论数', '说说内容']
values.append(value_head)

friends_values = []
friends_value_head = ['qq号码', 'qq昵称', '亲密指数']
friends_values.append(friends_value_head)

# login_flag = False     # flag 是不是python关键字   全局变量不可修改


def get_friends(path):



    testexist(path)
    try:
        # 设置等待网页加载的时间，直到抛出错误 time_to_wait:等待时间，以秒为单位
        driver.set_page_load_timeout(10)
        # 打开我的好友页面
        driver.get('http://user.qzone.qq.com/{}/myhome/friends'.format(username))
        time.sleep(3)

    except:
        print(u'网页启动异常，请重新打开')
        time.sleep(2)
        driver.quit()
    try:
        driver.find_element_by_id('login_div')
    except:
        print(u"非好友无法进入空间无权限抓取内容")

        driver.quit()
    else:
        # 登录QQ空间
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()  # 选择用户名框
        driver.find_element_by_id('u').send_keys(username)  # 输入个人登录账号
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(password)  # 输入个人登录密码
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
        # 设置一个超时时间，隐式地等待元素的查找和命令的执行。每次会话中，这个函数只需要被调用一次。
    driver.implicitly_wait(3)

    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
    except:
        print
        u'空间加载异常，请重新打开'
        time.sleep(2)
        driver.quit()
    else:
        driver.switch_to.frame('app_canvas_frame')
        next_page = 'page'
        page = 1

        try:
            while next_page:
                print(u'正在抓取第%d页面内容······' % page)
                qqid = driver.find_elements_by_css_selector('.item-operate.clearfix')
                name = driver.find_elements_by_css_selector('.info-name')
                score = driver.find_elements_by_css_selector('.score')

                for id, n, s in zip(qqid, name, score):
                    qq = id.get_attribute('data-uin')
                    nick = n.text
                    love_index = s.text

                    # print(qq)
                    # print(nick)
                    # print(love_index)

                    value = []
                    value.append(qq)
                    value.append(nick)
                    value.append(love_index)

                    print(value)

                    # 构造一个二维list
                    friends_values.append(value)

                # 所有的driver.find xxx 返回的数据类型都是 WebElement 数据类型

                # 进入了死循环 一直打印最后一页的页面数据 ？

                next_page = driver.find_element_by_css_selector('.qz-button.btn-pager-next')

                #  爬到第7页下面都是重复！奇怪
                # next_page = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[5]/a[11]')

                # print(next_page)

                page = page + 1

                next_page.click()

                # 通过判断主动触发异常 因为第一页也有< 不可点击

                # last_page = driver.find_element_by_css_selector('.qz-button-disabled.qz-button.btn-pager-next')
                #
                # print(last_page)
                # if driver.find_element_by_css_selector('.qz-button-disabled.qz-button.btn-pager-next'):
                #     raise IndexError
                #
                # python3 的格式化输出
                if page == 16:
                    raise IndexError

                time.sleep(1)
                driver.implicitly_wait(1)

            driver.quit()
        except BaseException as e:

            # print(e)
            print(u'抓取到%d页面结束' % page)

            # print(values)
            save_values_toexcel(friends_values, path, 'index')

            print('朋友信息保存成功！')
            # 抓取完数据 关闭浏览器

            driver.quit()

def testexist(path):
    if not os.path.exists(path):
        w = xlwt.Workbook()
        w.add_sheet('Sheet1')
        w.save(path)
    else:
        os.remove(path)
        w = xlwt.Workbook()
        w.add_sheet('Sheet1')
        w.save(path)


# def write03_excel(大厅):
#     wb = xlwt.Workbook()  # 创建一个excel工作簿对象
#     sheet = wb.add_sheet('测试2003excel')  # 用工作普对象新建一个sheet
#     # 二维的excel表格 所以需要一个双层for循环
#     # 确定行列树  i,j list元素下标
#     for i in range(0, 4):
#         for j in range(0, len(value[i])):
#             sheet.write(i, j, value[i][j])  # 一个坐标放一个value
#
#     wb.save(current_path)
#     print('写入数据成功！')

def write_data(data1, data2, path):
    f = xlrd.open_workbook(path)
    sheet = f.sheet_by_name('Sheet1')
    src = copy(f)
    row = sheet.nrows
    src.get_sheet(0).write(row, 0, data1)
    src.get_sheet(0).write(row, 1, data2)
    src.save(path)


# 逐条追加 效率低下
def add_excel_data(times, shuos, path):
    wb = xlrd.open_workbook(path)  # 用wlrd提供的方法读取一个excel文件

    # sheets = wb.sheet_names()
    # sheet = wb.sheet_by_name(sheets[0])

    rows = wb.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数

    new_wb = copy(wb)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象

    new_sheet = new_wb.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet  注意这个是（0） 不是[0]

    # new_sheet.write(rows, 0, times)  # xlwt对象的写方法，参数分别是行、列、值
    #
    # new_sheet.write(rows, 1, shuos)

    # 加说明头
    if rows == 0:
        new_sheet.write(0, 0, 'tims')  # xlwt对象的写方法，参数分别是行、列、值

        new_sheet.write(0, 1, 'shuos')

        new_sheet.write(rows + 1, 0, times)  # xlwt对象的写方法，参数分别是行、列、值

        new_sheet.write(rows + 1, 1, shuos)

    else:
        new_sheet.write(rows, 0, times)  # xlwt对象的写方法，参数分别是行、列、值

        new_sheet.write(rows, 1, shuos)

    new_wb.save(path)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel
    # print('数据追加成功!')


# 将所有的数据临时放到一个list的二维集合，抓取所有页面后 一次性写入
def save_values_toexcel(values, path, sheetname):
    wb = xlwt.Workbook()  # tab 自动没有（）
    sheet = wb.add_sheet(sheetname)
    rows = len(values)
    cols = len(values[0])

    for i in range(0, rows):
        for j in range(0, cols):
            sheet.write(i, j, values[i][j])
    wb.save(path)


def get_qq():
    wb = xlrd.open_workbook(qq_love_index_path)
    # sheet = wb.sheet_names()[0]     # 直接这种写 有问题的

    sheets = wb.sheet_names()
    sheet = wb.sheet_by_name(sheets[0])
    rows = sheet.nrows
    cols = sheet.ncols

    for i in range(1, rows):
        for j in range(0, 1):
            # print(sheet.cell_value(i, j), '\t', end='')
            print(sheet.cell_value(i, j))

            qqid = sheet.cell_value(i, j)
            get_shuoshuo(qqid, work_path)

        # print()


if __name__ == '__main__':
    # work_path=raw_input(u'请输入存储数据路径--excle表格类型')2571278041

    # 获取所有qq好友 亲密度
    get_friends(qq_love_index_path)

    # 获取 指定qq号的说说信息
    # get_shuoshuo('1453817380', work_path)  # 输入好友QQ号

    # 从excel中读取qq号码


    # 测试 追加写入excel模块
    # add_excel_data(
    # 测试 一次性写入excel模块
    # values = [['a',
    # save_values_toe
