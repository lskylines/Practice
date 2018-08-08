import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
from scipy.misc import imread



def get_text():
    with open('shengping.txt', 'r') as f:       #读取文本文件
        lines = f.read()
    my_text = '/'.join(jieba.cut(lines))     #取出文本，取出标点符号
    return my_text


def Show_image(my_text):
    bg_pic = imread('huge.jpg') #背景图
    word_cloud = WordCloud(mask=bg_pic, background_color='black', font_path="SimHei.ttf", scale=1.5)   #mask设置词云形状 ,font_path字体设置
    word_cloud.generate(my_text)
    image_color = ImageColorGenerator(bg_pic)
    plt.imshow(word_cloud, interpolation='bilinear')    #绘制词云
    plt.axis('off')
    plt.show()  #展现生成的词云


    word_cloud.to_file('test.jpg')    #将生成的词云图片保存


def main():
    my_text = get_text()
    Show_image(my_text)

if __name__ == "__main__":
    main()
