# -*- coding: utf-8 -*-
import jieba

import matplotlib.pyplot as plt

from wordcloud import WordCloud, ImageColorGenerator


def cut_word():
    # 打开本体TXT文件  读取中文时 要设置编码

    file_path = 'ts.txt'
    text = open(file_path, encoding='utf-8').read()

    # type(var) 输出变量类型
    # print(type(text))
    # print(text)

    # 结巴分词 cut_all=True 设置为全模式
    wordlist = jieba.cut(text, cut_all=True)

    # 使用空格连接 中文分词
    wl_space_split = " ".join(wordlist)
    # print(wl_space_split)

    # 将分词后的内容写入txt文件
    # with open('cutword.txt','w+',encoding='utf-8') as f:
    #     f.write(wl_space_split)


def draw_wordcloud():
    # 对分词后的文本生成词云

    # 读入自定义词云背景图片
    bg_img = plt.imread('bg2.jpg')

    # 设置词云
    my_wordcloud = WordCloud(
        background_color='white',  # 设置背景色
        mask=bg_img,  # 设置背景图片
        # max_words=2000, # 设置最大显示的字数
        stopwords="",  # 设置停用词
        font_path='simhei.ttf',  # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
        max_font_size=50,  # 设置字体最大值
        random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
        width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
    )

    # 生成词云

    # 直接读取以保存的分词文件
    cutword = open('cutword.txt', encoding='utf-8').read()
    myword = my_wordcloud.generate(cutword)

    # myword = my_wordcloud.generate(wl_space_split)

    # # 显示自定义图片北京词云
    # image_colors = ImageColorGenerator(bg_img)
    # myword.recolor(color_func=image_colors)

    # WordCloudDefautColors 只按照背景图片形状

    # 显示词云图
    plt.imshow(myword)

    # 是否显示x轴、y轴下标
    plt.axis("off")

    # 显示
    plt.show()

    # 保存图片
    # myword.to_file('wcp.jpg')

    # "WordCloudColorsByImg.png 颜色按照背景图片颜色布局生成
    # 显示自定义图片背景词云
    image_colors = ImageColorGenerator(bg_img)
    myword.recolor(color_func=image_colors)
    plt.imshow(myword)
    plt.axis("off")
    # 绘制背景图片为颜色的图片
    plt.figure()
    plt.imshow(bg_img, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    draw_wordcloud()
