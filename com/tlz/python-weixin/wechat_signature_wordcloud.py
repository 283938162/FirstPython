import re

import pyecharts
import itchat
import jieba

# 这里调用pyecharts来作词云 是不适用之前使用的worcloud包
from pyecharts import WordCloud

text_all = ''
itchat.auto_login(hotReload = True)

friends = itchat.get_friends(update = True)

ltext = []
for friend in friends:
	signnture_raw = friend['Signature'].strip().replace('emoji', '').replace('span', '').replace('class', '')

	# 由于表情都在<>  替换过滤掉
	signnture = re.sub(r'<[^>]*>', '', signnture_raw)
	print(friend['NickName'])
	print(signnture)
	ltext.append(signnture)

text_all = ''.join(ltext)
wc_jieba = jieba.cut(text_all, cut_all = True)
# 以 空格 为间隔 将分词后的内容连接起来
wl_split = ' '.join(wc_jieba)

print(wl_split)

word_list = []
word_count_list = []

word_list_raw = wl_split.split(' ')
print(word_list)

# 设置停用词库
stop_word = ['的', '一', ' ', '不']

# stop_d = re.findall(r'\d+')

for x in word_list_raw:
	if x in stop_word:
		continue
	if wl_split.count(x) == 1044:
		continue
	print(x, wl_split.count(x))
	word_list.append(x)

	word_count_list.append(wl_split.count(x))

print(word_list)
print(word_count_list)

wordcloud = WordCloud(width = 1300, height = 620)

# 词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward','triangle', 'pentagon', 'star'可选。
wordcloud.add("", word_list, word_count_list, word_size_range = [20, 100])

wordcloud.render()
