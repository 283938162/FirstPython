from telnetlib import EC

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Selenium是一个自动化测试工具，支持驱动多种浏览器，爬虫中主要用来解决JavaScript渲染问题，
跳转，输入啦，点击，下拉等等操作。当无法从网页中静态获取内容时，则可以用这个工具。
'''
#
url = 'https://www.taobao.com'
phantomjs_path = '/Users/anus/local/phantomjs-2.1.1-macosx/bin/phantomjs'
#
# url = 'http://music.163.com/#/playlist?id=317113395'
# # executable_path 为你安装phantomJS的可执行的文件路径
# driver = webdriver.PhantomJS(executable_path=phantomjs_path)
# driver.maximize_window()  # 设置全屏
#
# driver.get(url)  # 执行js
#
# # 网易云采取了框架，所以必须要加上这一句，就可以返回框架的源代码了
# driver.switch_to.frame(driver.find_element_by_name("contentFrame"))
#
# html = driver.page_source  # 将浏览器执行后的源代码付给html
#
# # print(html)

'''
实现浏览器的自动操作
自动打开浏览器
自动搜索关键词 python3
自动关闭浏览器
'''

# 完成了一个浏览器对象的初始化，接下来我们要做的就是调用browser对象，让其执行各个动作，就可以模拟浏览器操作了。

# 要下载安装对应平台浏览器的驱动
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('python3')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 100)
#
#     # 等待id=content_left的元素被加载进来
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#
#     # 打印网页源码
#     # print(browser.page_source)
# finally:
#     # 关闭浏览器，若不关闭，浏览器则会在后台一直运行下去
#     browser.close()


'''
我们可以用get()方法来请求一个网页，参数传入链接URL即可，
比如在这里我们用get()方法访问淘宝，然后打印出源代码，代码如下：
'''

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')  # 并没有对应的post
#
# print(browser.get_cookies())
# browser.close()

'''
查找元素

单种元素
多种元素

'''

#
# try:
#     browser.get('http://www.taobao.com')
#
#     #单个元素获取搜索框
#     input_first = browser.find_element_by_id('q')
#
#     #多个元素
#     lis = browser.find_element_by_class_name('nav-hd')
#     print(lis)
# finally:
#     browser.close()

'''
元素交互操作
'''

# try:
#     browser = webdriver.Chrome()
#     browser.get(url)
#
#     input = browser.find_element_by_id('q')
#     input.send_keys('Macbook Pro')
#     time.sleep(1)
#     input.clear()
#
#     input.send_keys('iPhone')
#
#     # button = browser.find_element_by_class_name('btn-search')
#     # button.click()
#
#     # 通过回车开始检索
#     input.send_keys(Keys.ENTER)
#
# finally:
#     browser.close()


'''
交互动作
'''

# browser = webdriver.Chrome()
# try:
#     url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
#     browser.get(url)
#     browser.switch_to.frame('iframeResult')
#
#     # source = browser.find_elements_by_css_selector('#draggable')   # 错误的写法
#     # target = browser.find_elements_by_css_selector('#droppable')
#
#     source = browser.find_element_by_css_selector('#draggable')
#     target = browser.find_element_by_css_selector('#droppable')
#
#     actions = ActionChains(browser)
#     actions.drag_and_drop(source, target)
#     actions.perform()
#
#     time.sleep(10)
# finally:
#     browser.close()


'''
控制滚动条
'''
# 访问百度
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# #搜索
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# time.sleep(3)
#
# #将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(3)
#
#
# #将滚动条移动到页面的顶部
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# time.sleep(3)
#
# driver.quit()


'''
qq 空间翻页  如和长距离翻页
'''
#
# url = 'https://www.iplaysoft.com/'
#
# qq_url = 'https://user.qzone.qq.com/1353154474'
# driver = webdriver.Chrome()
# driver.get(url)
#
# # driver.find_element_by_id('QM_Feeds_Iframe')
# time.sleep(3)
#
# # 将页面滚动条拖到底部
# js = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(10)
#
#
# # 将滚动条移动到页面的顶部
# # js="var q=document.documentElement.scrollTop=0"
# # driver.execute_script(js)
# # time.sleep(3)
#
# driver.quit()


'''
一个动态加载的直播网站的例子
https://www.huomao.com/channel/lol
'''

driver = webdriver.Chrome()

url = "https://www.huomao.com/channel/lol"

#司机开车了
driver.get(url)

#让页面移到最下面点击加载，连续6次，司机会自动更新！！
# for i in range (6):
#     driver.find_element_by_class_name('getmore getmore0 hidden').find_elements_by_tag_name('a').click()
#     time.sleep(1)
#
#
# js="document.body.scrollTop=1000"
# driver.execute_script(js)

# 3 让页面滚动到下面  结局上面的bug a  这里至关重要！！！  与上面js的区别
driver.execute_script("window.scrollBy(0,3000)")
time.sleep(3)

driver.execute_script("window.scrollBy(0,5000)")
time.sleep(3)