import pandas as pd
import matplotlib.pyplot as plt


def data_process(file):
    # 从 csv 文件读取抓取到的结果，指定第一行为各个列的名称
    df = pd.read_csv(file)

    df_author_voteup = df.loc[:, ['作者UP主(author)', '播放量(play_count)']]

    # 以 题目(title) 列进行分组
    grouped = df_author_voteup.groupby('作者UP主(author)').sum()

    # 对分组进行求和并查看 voteup_count 列的求和结果
    voteup = grouped['播放量(play_count)']

    # 对求和结果进行降序排列并取出前十
    all_authors = voteup.sort_values(ascending=False)

    top_10_authors = all_authors[0:10]

    return top_10_authors


def visualize(df):
    # 加载中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 初始化图表绘图区域
    plt.figure(figsize=[10.0, 4.0])

    # 直接使用 pandas 提供的绘图接口绘图
    df.plot.barh()

    # 从上到下顺序输出 y 轴
    plt.gca().invert_yaxis()

    # 显示绘制好的图标
    plt.show()


if __name__=='__main__':
    df = data_process('answers.csv')
    visualize(df)