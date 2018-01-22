from urllib import parse

import requests
import json
import re
import sys
import os

saveFolder = 'image'
imageSizeName = [None, None, '1024x768', '1280x720', '1280x1024', '1440x900', '1920x1080', '1920x1200', '1920x1440']

workList_url = "http://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi"

'''

http%3A%2F%2Fshp%2Eqpic%2Ecn%2Fishow%2F2735012211%2F1516590355%5F84828260%5F8310%5FsProdImgNo%5F1%2Ejpg%2F200
数据在传输过程中进行了加密 urllib.parse.quote(url)  解析处理过的urllib.parse.unquote(url)

'''


def get_list(page_id):
    # 参数集合 是字典形式
    worklist_params = {
        "activityId": "2738",
        "sVerifyCode": "ABCD",
        "sDataType": "JSON",
        "iListNum": "20",
        "totalpage": "0",
        "page": page_id,
        "iOrder": "0",
        "iSortNumClose": "1",
        "jsoncallback": "jQuery17101954572044754206_1513821397041",
        "iAMSActivityId": "51991",
        "_everyRead": "true",
        "iTypeId": "2",
        "iFlowId": "267733",
        "iActId": "2735",
        "iModuleId": "2735",
        "_": "1513821606943"
    }
    result = requests.get(workList_url, params=worklist_params)

    # 提取json部分
    # worklist_raw = result.text
    # worklist_json = worklist_raw[(worklist_raw.find('(') + 1):(len(worklist_raw) - 2)]
    # worklist = json.loads(parse.unquote(worklist_json))
    #
    info_json = re.findall(r'\((.*)\)', result.text)[0]
    # worklist = json.loads(info_json)
    worklist = json.loads(parse.unquote(info_json))
    return worklist


# print(get_list(0))

def download_img(url, path):
    try:
        image_data = requests.get(url, timeout=15)
    except Exception as e:
        print('下载图片出错,%s,%s' % (e, url))
        return False

    # wb（b 二进制））与w 与a（追加）
    with open(path, 'wb') as f:
        # 图片保存时 写入的是get到对象的content内容
        f.write(image_data.content)
    return True


def makedir(*dirname):
    # os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
    dirpath = os.path.join(sys.path[0], *dirname)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)


def download_list(list):
    makedir(saveFolder)
    for item in list['List']:  # 循环json的中List字段
        makedir(saveFolder, item['sProdName'])
        print("创建文件夹(%s)" % item['sProdName'])

        # 为啥循环要从2开始到9 没有no_0  1是缩略图 直接舍弃
        for i in range(2, 9):
            node_name = 'sProdImgNo_' + str(i)
            image_rawurl = item[node_name]
            # image_url = image_rawurl[:len(image_rawurl) - 3] + '0'
            image_url = image_rawurl.replace('/200', '/0')
            print(image_url)

            image_savepath = os.path.join(sys.path[0], saveFolder, item['sProdName'],
                                          item['sProdName'] + '_' + imageSizeName[i] + '.jpg')
            if download_img(image_url, image_savepath):
                print('成功下载图片：%s, 尺寸：%s' % (item['sProdName'], imageSizeName[i]))


if __name__ == '__main__':
    for i in range(1):
        list = get_list(i)
        download_list(list)
