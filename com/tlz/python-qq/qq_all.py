# coding:utf-8
from selenium import webdriver
import time, os
import xlrd, xlwt
from xlutils.copy import copy
import re
import queue
import threading

'''
测试爬取所有qq

爬取并存入excel

未抓取 设备名称，评论内容

'''

# 使用selenium
# 使用selenium的隐藏PhantimJS浏览器登陆账号后对内容获取
# 注意frame与iframe的格式框切换
# driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver = webdriver.Chrome()
driver.maximize_window()
# driver.set_preference('network.proxy.type', 1)
# driver.set_preference('network.proxy.http', '127.0.0.1')
# driver.set_preference('network.proxy.http_port', 17890)

username = ''
password = ''

work_path = '/Users/anus/PycharmProjects/FirstPython/com/tlz/python-qq/data/qq.xls'
qq_love_index_path = '/Users/anus/PycharmProjects/FirstPython/com/tlz/python-qq/data/qq_love_index.xls'

values = []

# 加头
value_head = ['qq号码', 'qq昵称', '发表时间', '点赞数', '评论数', '说说内容']
values.append(value_head)


def login_qq():
    try:
        # 设置等待网页加载的时间，直到抛出错误 time_to_wait:等待时间，以秒为单位
        driver.set_page_load_timeout(10)
        driver.get('http://user.qzone.qq.com')
        time.sleep(3)
    except:
        print(u'网页启动异常，请重新打开')
        time.sleep(2)
        driver.quit()
    try:
        driver.find_element_by_id('login_div')
    except:
        print("好友未向你开放空间权限,无法抓取内容")
        driver.quit()
    else:

        driver.switch_to.frame('login_frame')
        try:
            # time.sleep(3)
            # qq 在线的话 快速登录
            print('检测到qq在线，快速登录')
            driver.find_element_by_css_selector('.face').click()
        except:
            # 密码登录QQ空间
            print('密码登录')
            driver.find_element_by_id('switcher_plogin').click()
            driver.find_element_by_id('u').clear()  # 选择用户名框
            driver.find_element_by_id('u').send_keys(username)  # 输入个人登录账号
            driver.find_element_by_id('p').clear()
            driver.find_element_by_id('p').send_keys(password)  # 输入个人登录密码
            driver.find_element_by_id('login_button').click()

        time.sleep(3)
    # 设置一个超时时间，隐式地等待元素的查找和命令的执行。每次会话中，这个函数只需要被调用一次。
    driver.implicitly_wait(3)

    # 有时候需要拖动验证码
    time.sleep(4)

    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
    except:
        print
        u'空间加载异常，请重新打开'
        time.sleep(2)
        driver.quit()


def get_user_info():
    driver.switch_to.frame('app_canvas_frame')
    #    last_page=driver.find_element_by_css_selector('.mod_pagenav')
    #    page_num=re.findall('\d+',last_page.text)[-1]
    next_page = 'page'
    page = 1

    # 设置一个超时时间，隐式地等待元素的查找和命令的执行。每次会话中，这个函数只需要被调用一次。
    # driver.implicitly_wait(1)  # 防止第一页抓空

    try:
        while next_page:
            print(u'正在抓取第%d页面内容······' % page)

            q_author = driver.find_elements_by_css_selector('.qz_311_author.c_tx.nickname.goProfile')
            content = driver.find_elements_by_css_selector('.content')
            stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')

            # 因为该class 存在多个相同的值 不能使用常见的css选择器定位 可以通过下面 便签[属性值] 的方法来定位
            # qz_like = driver.find_elements_by_css_selector('.qz_like_btn.c_tx.mr8'")
            # qz_like = driver.find_elements_by_css_selector("input[class='qz_like_btn c_tx mr8'][_origtemp='赞{cnt}']")

            qz_like = driver.find_elements_by_css_selector('a[_origtemp]')

            qz_comment = driver.find_elements_by_css_selector('.c_tx.comment_btn')

            # 发表设备 大多为空 不好并行迭代
            # try:
            #     custom_tail = driver.find_elements_by_css_selector('.custom-tail')
            # except BaseException as e:
            #     custom_tail = ''

            # 并行迭代 里面的list必须不能为空
            for aut, con, sti, li, ct in zip(q_author, content, stime, qz_like, qz_comment):
                # 字典
                # data = {
                #     'time': sti.text,
                #     'shuos': con.text
                # }
                #
                # qq = q_author.__getattribute__('data-uin')

                author = aut.text
                qqid = aut.get_attribute('data-uin')
                shuos = con.text
                times = sti.text

                # like = li.text
                # comment = ct.text

                # 提取点赞数和评论数
                # 在Python中，None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False。除此之外的其它对象都会被转化成True
                if re.findall(r'\d+', li.text):
                    like = re.findall(r'\d+', li.text)[0]
                else:
                    like = 0

                if re.findall(r'\d+', ct.text):
                    comment = re.findall(r'\d+', ct.text)[0]
                else:
                    comment = 0

                # if custom_tail is None:
                #     tail = '未获取到该设备'
                # else:
                #     tail = ta.text

                # print(qq)
                # print(author)
                # print(times)
                # print(shuos)
                # print(like)
                # print(comment)

                # print(tail)

                value = []
                value.append(qqid)
                value.append(author)
                value.append(times)
                value.append(like)
                value.append(comment)
                value.append(shuos)

                print(value)

                # 构造一个二维list
                values.append(value)

                # print('times:' + times + '\t shuos:' + shuos)
                # write_data(data['time'], data['shuos'], path)
                # add_excel_data(times, shuos, path)

            # 所有的driver.find xxx 返回的数据类型都是 WebElement 数据类型
            next_page = driver.find_element_by_link_text(u'下一页')
            page = page + 1

            # python3 的格式化输出
            # print(u'正在抓取第%d页面内容······' % page)

            next_page.click()

            time.sleep(5)
            driver.implicitly_wait(3)
        # driver.quit()
    except BaseException as e:

        # print(e)
        print('抓取到%d页面结束' % page)

        # print(values)
        # save_values_toexcel(values, path, values[0][1])

        # print('说说信息保存成功！')
        # 抓取完数据 关闭浏览器

        # driver.quit()


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


def open_qq_zone(qq):
    try:
        # 设置等待网页加载的时间，直到抛出错误 time_to_wait:等待时间，以秒为单位
        driver.set_page_load_timeout(10)
        url = 'http://user.qzone.qq.com/{}/311'.format(qq)
        driver.get(url)

        # # 浏览器 新窗口打开连接 Tab
        # new_window = 'window.open("'+url+'")'
        # print(new_window)
        #
        # driver.execute_script(new_window)
        # # 移动句柄，对新打开页面进行操作
        # driver.switch_to.window(driver.window_handles[1])

        time.sleep(3)
    except:
        print('网页启动异常，请重新打开')
        time.sleep(2)
        driver.quit()
    else:
        # get_user_info()
        print('开始抓取...')


def get_qq():
    qq_list = []
    wb = xlrd.open_workbook(qq_love_index_path)
    # sheet = wb.sheet_names()[0]     # 直接这种写 有问题的

    sheets = wb.sheet_names()
    sheet = wb.sheet_by_name(sheets[0])
    rows = sheet.nrows
    cols = sheet.ncols

    for i in range(1, rows):
        for j in range(0, 1):
            # print(sheet.cell_value(i, j), '\t', end='')
            # print(sheet.cell_value(i, j))
            qqid = sheet.cell_value(i, j)
            qq_list.append(qqid)
    return qq_list


def list_to_queue():
    qq_list = get_qq()
    # print(qq_list)

    for i in qq_list:
        q.put(i)
    return q


def run():
    # print(q.get())

    qq = q.get()
    print(qq)

    # q.task_done()
    time.sleep(3)


def main():
    for i in range(5):
        t = threading.Thread(target=run)
        # t.setDaemon(True)
        t.start()

    t.join()


if __name__ == '__main__':
    # qq_list = []
    # qq_list = get_qq()
    # print(qq_list)
    #
    # start = time.time()
    # login_qq()
    # page = 1
    # # qq_list = ['1353154474', '283938162']
    # for x in qq_list:
    #     print('开始抓取第{}位用户，该用户的QQ号码为 {}'.format(page, x))
    #     open_qq_zone(x)
    #     page += 1
    #     time.sleep(3)
    #
    # print('qTime = %s' % (time.time() - start))
    q = queue.Queue()
    q = list_to_queue()

    start = time.time()
    main()
    print('qTime = %s' % (time.time() - start))

    driver.close()
