'''

该程序的主要功能是监控撤回消息，并且如果有消息撤回就会撤回的消息发送给你
'''
import re

import itchat
from itchat.content import *
import sys
import time
import os

msg_information = {}  ##将信息存储在字典中，每一个msg_id对应一条信息


#  这些注册消息方法 怎么被调用的？？？


@itchat.msg_register(TEXT, isFriendChat = True, isGroupChat = True, isMpChat = True)
def handle_revice_msg(msg):
	msg_time_rec = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

	# 由于只能获取发送消息好友的UserName 所以逆向获取昵称
	msg_from = itchat.search_friends(userName = msg['FromUserName'])['NickName']
	msg_time_send = msg['CreateTime']  # 消息发送的时间 跟上面 接受到消息的时间区别？

	msg_id = msg['MsgId']  # 每条消息的id

	msg_content = msg['Text']  # 存储消息的内容

	msg_type = msg['Type']

	print(msg_type, msg_time_rec, msg_time_send, msg_id, msg_content)

	# 将 信息 存储 在字典里面,每一个msg_id对应一条信息

	msg_information.update(
		{
			msg_id: {
				'msg_from': msg_from,
				'msg_time_send': msg_time_send,
				'msg_time_rec': msg_time_rec,
				'msg_type': msg_type,
				'msg_content': msg_content

			}
		}
	)


## 这个用于监听是否有消息测回

@itchat.msg_register(NOTE, isFriendChat = True, isGroupChat = True, isMpChat = True)
def information(msg):
	# msg['Content'] 包含所有消息类型
	# 如果msg['Content']中包含消息测回和id，就执行下面的语句
	if '你撤回了一条消息' in msg['Content']:
		old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)  # 在返回的content查找撤回的消息的id
		old_msg = msg_information.get(old_msg_id)  # 得到消息
		print(old_msg)

		msg_body = "告诉你一个秘密~" + "\n" \
				   + old_msg.get('msg_from') + " 撤回了 " + old_msg.get("msg_type") + " 消息" + "\n" \
				   + old_msg.get('msg_time_rec') + "\n" \
				   + "撤回了什么 ⇣" + "\n" \
				   + r"" + old_msg.get('msg_content')

		print(msg_body)

		# 将撤回的消息发送到文件助手
		itchat.send_msg(msg_body, toUserName = 'filehelper')

		# 删除字典就消息
		msg_information.pop(old_msg_id)


if __name__ == '__main__':
	itchat.auto_login(hotReload = True)
	itchat.run()
