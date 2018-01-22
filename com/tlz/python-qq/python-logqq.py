from bs4 import BeautifulSoup
from selenium import webdriver
import time

'''
存在问题：a.抓取到重复的页面？ 原因未知 可以是下一页还没加载 完  又再次爬取
        （1） 执行js 滑动页面向下
        （2） 翻页后强行等待一会 time.sleep(3)
        b.有时候需要登录需要拖动验证
        c.无头浏览器 有问题

         
'''

# 使用selenium
# driver = webdriver.PhantomJS(executable_path="/Users/anus/local/phantomjs-2.1.1-macosx/bin/phantomjs")
driver = webdriver.Chrome()
driver.maximize_window()


# 登录QQ空间
def get_shuoshuo(qq):
    driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
    # time.sleep(2)

    # 判断是否登录
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()  # 选择用户名框
        driver.find_element_by_id('u').send_keys('')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('')
        driver.find_element_by_id('login_button').click()
        time.sleep(5)
    driver.implicitly_wait(3)

    # 用户是否设置了访问权限
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False
    if b == True:
        driver.switch_to.frame('app_canvas_frame')

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        pages = soup.find('a', title='末页').span.text
        print(pages)

        for x in range(0, int(pages) + 1):

            # 可以隐式等待，等翻页读取完毕才执行下一个步骤。
            # driver.implicitly_wait(3)

            print('page =', x + 1)


            # 3 让页面滚动到下面  结局上面的bug a  这里至关重要！！！
            # driver.execute_script("window.scrollBy(0,3000)")
            # time.sleep(3)
            #
            # driver.execute_script("window.scrollBy(0,5000)")
            # time.sleep(3)

            #  等同于上面  都是后限于网速 一点一点移动会更好一点 但效率也就低
            driver.execute_script("window.scrollBy(0,10000)")
            time.sleep(3)


            html = driver.page_source

            soup = BeautifulSoup(html, 'lxml')

            contents = soup.find_all('pre', class_='content')
            times = soup.find_all('a', class_='c_tx c_tx3 goDetail')

            # print(contents)
            # print(times)

            for con, sti in zip(contents, times):
                data = {
                    'time': sti.text,
                    'shuos': con.text
                }
                print(data)

                # with open('shuos.txt', 'a', encoding='utf-8') as f:
                #     f.write('time:'+sti.text+ "\n content:"+con.text+"\n")
                #     f.write("----------------------")

            try:
                # 自动翻页
                driver.find_element_by_link_text('下一页').click()
            except BaseException as e:
                # 如果到达最后一页 跳出循环
                print("已经到达最后一页了")
                break
    # 查找当前会话中所有的cookies 如果找到了就返回一个dictionaries对象，包含所有cookies
    cookie = driver.get_cookies()

    # cookie_dict:字典对象，必要的keys有“name”和“value”，可选的keys有path”, “domain”,“secure”, “expiry”
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1};".format(c['name'], c['value'])
        cookie_dict.append(ck)
    i = ''
    for c in cookie_dict:
        i += c
    print('Cookies:', i)
    print("==========完成================")

    driver.close()
    driver.quit()


if __name__ == '__main__':
    get_shuoshuo('283938162')
