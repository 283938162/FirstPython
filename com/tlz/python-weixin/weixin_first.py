import itchat, time
import datetime

'''
itchat.auto_login() 这种方法将会通过微信扫描二维码登录，但是这种登录的方式确实短时间的登录，
并不会保留登录的状态，也就是下次登录时还是需要扫描二维码，如果加上hotReload==True,那么就会保留登录的状态，
至少在后面的几次登录过程中不会再次扫描二维码，该参数生成一个静态文件itchat.pkl用于存储登录状态
'''
itchat.auto_login(hotReload=True)
itchat.dump_login_status()


# itchat.auto_login()

# 先登录
# itchat.login()

def get_curr_time(toUserName):
    curr_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(curr_time)
    return curr_time


def messageToX(userName):
    message = get_curr_time(userName) + '\n来自alpha-beta的message,仅做测试用/:kotow'
    return message


# itchat.send(curr_time, 'filehelper')

# 如果不指定用户名 发送不成功！
# print(itchat.send("Hello World!"))


# false
# itchat.send_msg("hello 没有指定用户名!",'')

# 必须要指定用户名 ok
# itchat.send_msg("hello 指定用户名!",'filehelper')
#


# 向自己的 微信 发送消息失败
# itchat.send("Hello World!", toUserName='alpha-beta')


# 向自己的 文件助手 发送成功

# itchat.send(curr_time, toUserName='filehelper')
# itchat.send(u'你好', toUserName='filehelper')
# itchat.send(u'你好,没有使用toUserName', 'filehelper')
# itchat.send('你好,没有使用u', 'filehelper')
#
# itchat.send('@fil@%s' % 'itchat.pkl', 'filehelper')
#
# # ok
# itchat.send('@img@%s' % '1.png', 'filehelper')
# false
# itchat.send('@img@%s' % 'QR.png', 'filehelper')


#  还是要指明发送 send发图片是消息形似（文件还是文件） send_file是文件形式
# itchat.send_file('1.png','filehelper')
# itchat.send_image('1.png', 'filehelper')

'''
以上都是都给自己的文件助手  


怎么发给自己微信列表里的好友或者公众号发消息呢？

'''


# 单发

def sendMsgTofriend():
    # 想给谁发信息，先查找到这个朋友,name参数为微信列表备注
    users = itchat.search_friends(name=u'肥宝')
    # 获取好友全部信息,返回一个列表,列表内是一个字典
    # print('user-info=%s' % users)

    # #获取`UserName`,用于发送消息
    # userName 的形式  @26aca5266fbfb80ec4429b6df2fcdf2f89bab3d89ba34af96ff9d1c8dacd9cb9
    userName = users[0]['UserName']

    print(userName)
    # 然后给他发消息
    # get_curr_time(userName)

    # message = get_curr_time(userName) + '\n来自alpha-beta的message,仅做测试用/:kotow'
    # itchat.send(message, userName)

    # 向我发送文本消息 使用read方法是原格式发给微信好友
    # f = open('tt', encoding='utf-8').read()
    # itchat.send(f, userName)

    # 发送文件
    itchat.send('@fil@%s' % 'itchat.pkl', userName)


# sendMsgTofriend()


# 群发

def sendMsgToAllFriends():
    # 获取所有好友信息
    accounts = itchat.get_friends()
    print(accounts)

    # 获取自己的信息
    userName = accounts[0]['UserName']
    print(userName)

    itchat.send_msg(messageToX(userName), userName)

    # 向所有好友发送信息

    # for account in accounts:
    #     userName = account['UserName']
    #     print(userName)
    #
    #     # 将时间和消息做成一条
    #     itchat.send(message, userName)


sendMsgToAllFriends()

# 发公众号

def sendMsgToOfficesAccount():
    mps = itchat.get_mps()

    # 获取所有公众号的name
    print([x['NickName'] for x in mps])  # 优雅

    # 也就是按公众号名称查找,返回值为一个字典的列表
    mps_single = itchat.search_mps(name='Crossin的编程教室')
    print(mps_single[0]['UserName'])

    userName = mps_single[0]['UserName']

    message = '微博'
    itchat.send(message, userName)


# sendMsgToOfficesAccount()

# （1） 向群里发消息
#  (2) 分别向群里每个成员发消息


def sendMsgToChatRoom():
    # chatrooms = itchat.get_chatrooms

    # 微信创建群之后 一定要保存到通讯录才能输出群的信息 不然是一个空列表 []
    chatrooms = itchat.get_chatrooms()

    print(chatrooms)

    #  向群内发消息
    # userName = chatrooms[0]['UserName']
    # itchat.send(messageToX(userName), userName)

    # 打印所有群昵称
    # print([x['NickName'] for x in chatrooms])

    # 统计群成员分别信息 多层嵌套集合
    for x in chatrooms:
        # print(x['MemberList'])
        for x in x['MemberList']:
            # print(x['NickName'])

            # 给群里的每个成员分别发送消息
            userName = x['UserName']

            itchat.send(messageToX(userName),userName)



# sendMsgToChatRoom()
