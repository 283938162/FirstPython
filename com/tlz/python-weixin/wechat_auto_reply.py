import itchat
from itchat.content import *  # 如果不加 下面的TEXT 要写全称


# 封装好的装饰器，当接收到的消息是Text，即文字消息

# 给自己发消息不会自动回复
# @itchat.msg_register(itchat.content.TEXT)
# def simple_reply(msg):
# 	# 这个是向发送者发送消息
# 	itchat.send_msg('已经收到了文本消息，消息内容为%s' % msg['Text'], toUserName = msg['FromUserName'])
#
# 	# 返回的给对方的消息，msg["Text"]表示消息的内容
# 	return "T reveived: %s" % msg["Text"]


@itchat.msg_register(TEXT, isFriendChat = True, isGroupChat = True, isMpChat = True)
def text_reply(msg):
	# msg.user.send("%s : %s" % (msg.type, msg.text))

	return ("%s : %s" % (msg.type, msg.text))






if __name__ == '__main__':
	itchat.auto_login(hotReload = True)
	itchat.run()
