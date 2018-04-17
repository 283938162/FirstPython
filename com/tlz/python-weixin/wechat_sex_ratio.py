import itchat

import pyecharts

from pyecharts import *
from pyecharts.charts import bar

'''
统计微信所有好友 性别比例
'''

# 登录 加参数表示 不用频换的每次登录 会临时保存登录信息
itchat.auto_login(hotReload = True)

'''


每个好友为一个字典, 其中第一项为本人的账号信息;
传入 update=True, 将更新好友列表并返回, get_friends(update=True)

'''

# 默认 本来就是一个列表 全部  为啥还要多加这个呢 虽然意思还是列表中的所有元素[0:]

friends = itchat.get_friends(update = True)

# Sex  1 男 2 女


#  python 是否有else if ？

femaleNum = maleNum = otherNum = totalNum = 0

for friend in friends:
	if friend['Sex'] == 1:
		maleNum += 1
	else:
		if friend['Sex'] == 2:
			femaleNum += 1
		else:
			otherNum += 1

totalNum = len(friends)

print("你总共有{}位好友,\n其中男性好友{}人,女性好友{}人,其他{}人".format(totalNum, maleNum, femaleNum, otherNum))
# 调用pyecharts 进行饼状图展示

var = ['女性好友', '男性好友', '其他']
value = [femaleNum, maleNum, otherNum]
# Bar柱状图
# bar = Bar('我的好友性别数量', '微信')
# bar.add('性别', var, value)
# bar.show_config()
# bar.render()

# Pie饼状图

pie = Pie('微信好友性别比例')

pie.add('',var,value,is_label_show = True)

pie.show_config()

pie.render()
