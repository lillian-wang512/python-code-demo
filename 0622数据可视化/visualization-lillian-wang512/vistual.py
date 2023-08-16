import pandas as pd
import jieba
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# 从回答 csv 文件中提取出回答的文本并转化成列表
def get_answers(file):
    df = pd.read_csv(file)

    answers = df['题目(title)']
    # answers =','.join( df.values.tolist()
    return list(answers)


# 结巴分词的 TD-IDF 接口直接提取关键词和其权重
def get_keywords(content, topK):
    keywords = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    df = pd.DataFrame(keywords, columns=['keyword', 'weight'])
    return df


# 生成词云，注意这里的参数是一个字典 {'关键词': 12.123123} 后面的浮点数是权重
def generate_cloud(frequencies):
    wordcloud = WordCloud(
        'simfang.ttf',
        width=1920,
        height=1080,
        background_color='white',
        stopwords=STOPWORDS).generate_from_frequencies(frequencies)

    fig = plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud)
    plt.axis('off')  # 不显示坐标轴
    plt.tight_layout(pad=0)  # 不留空白
    plt.show()


if __name__ == '__main__':
    answers = get_answers('yangshixinwen.csv')

    jieba.analyse.set_stop_words(r'stopwords.txt')

    df = pd.DataFrame(columns=['keyword', 'weight'])
    for answer in answers:
        answer_keyword = get_keywords(answer, 10)
        df = df.append(answer_keyword)

    grouped = df.groupby('keyword').sum()

    keywords = grouped.sort_values('weight', ascending=False)

    top_100 = keywords[0:100]
    generate_cloud(top_100.weight.to_dict())
