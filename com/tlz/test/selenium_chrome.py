import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get('https://www.taobao.com')

#浏览器 新窗口打开连接 Tab
newwindow = 'window.open("https://www.baidu.com")'
driver.execute_script(newwindow)
#移动句柄，对新打开页面进行操作
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
# 关闭新打开的tab标签页
driver.close()

# for i in range(3):
#     driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
#     time.sleep(2)
# driver.get('https://www.baidu.com')

