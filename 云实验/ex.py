import re
from PIL import Image
import numpy as np
from wordcloud import ImageColorGenerator
from wordcloud import WordCloud
import matplotlib.pyplot as plt


with open('constitution.txt', encoding='utf-8') as c:
    # ‘’’抽取文本中的英文部分并小写化，并将空格作为分隔拼接为长字符串’’’
    text = ' '.join([word.group().lower()
                    for word in re.finditer('[a-zA-Z]+', c.read())])

# ‘’’查看前100个字符’’’
text[:200]


usa_mask = np.array(Image.open('美国地图蒙版星条旗色.png'))
image_colors = ImageColorGenerator(usa_mask)

# ‘’’从文本中生成词云图’’’
wordcloud = WordCloud(background_color='white',  # 背景色为白色
                      height=2000,  # 高度设置为400
                      width=1500,  # 宽度设置为800
                      scale=20,  # 长宽拉伸程度程度设置为20
                      prefer_horizontal=0.2,  # 调整水平显示倾向程度为0.2
                      mask=usa_mask,  # 添加蒙版
                      max_words=1000,  # 设置最大显示字数为1000
                      relative_scaling=0.3,  # 设置字体大小与词频的关联程度为0.3
                      max_font_size=60  # 缩小最大字体为80
                      ).generate(text)

plt.figure(figsize=[7, 4])
plt.imshow(wordcloud.recolor(color_func=image_colors), alpha=1)
plt.axis('off')
# ‘’’保存到本地’’’
plt.savefig('图10.jpg', dpi=600, bbox_inches='tight', quality=95)
plt.show()
