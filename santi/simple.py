from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random
import os
from PIL import Image
import numpy as np


font = 'DroidSansFallbackFull.ttf'      #使用的字体

def gray_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


d = path.dirname(__file__)


mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))  #背景图
 

text = open(path.join(d, u'santi2.txt')).read()  #将文件内容读取

text = text.replace("程心说", "程心")    
text = text.replace("程心和", "程心")
text = text.replace("程心问", "程心")

stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

# Generate a word cloud image

wc = WordCloud(font_path=font, max_words=2000, mask=mask, stopwords=stopwords, margin=10, random_state=1).generate(text)
 
default_colors = wc.to_array()
plt.title("Custom colors")     #图片标题
plt.imshow(wc.recolor(color_func=gray_color_func, random_state=3))
wc.to_file("a_new_hope.png")      #保存文件
plt.axis("off")
plt.figure()

plt.title("三体-词频统计")
plt.imshow(default_colors)
plt.axis("off")
plt.show()


