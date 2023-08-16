import requests
from bs4 import BeautifulSoup
import json
import csv
import codecs
import time

ua = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}





def url_element_get(video, video_info):
    url_element = video.select('div.info > div.headline.clearfix > a')
    video_info['title'] = url_element[0].text
    video_info['url'] = url_element[0]['href']
    return video_info


def play_count_element_get(video, video_info):
    play_count_element = video.select('div.info > div.tags > span.watch-num')
    video_info['play_count'] = play_count_element[0].text.strip()
    return video_info


def danmu_element_get(video, video_info):
    danmu_element = video.select('div.info > div.tags > span.hide')
    video_info['danmu_count'] = danmu_element[0].text.strip()
    return video_info


def upload_time_element(video, video_info):
    upload_time_element = video.select('div.info > div.tags > span.time')
    video_info['upload_date'] = upload_time_element[0].text.strip()
    return video_info


def up_url_element_get(video, video_info):
    up_url_element = video.select('div.info > div.tags > span > a.up-name')
    video_info['author'] = up_url_element[0].text
    video_info['author_url'] = up_url_element[0]['href']
    return video_info








def main():

    header = ['题目(title)', '网址(url)', '播放量(play_count)', '弹幕(danmu)',
                   '上传时间(upload_date)', '作者UP主(author)', 'UP主个人界面(author_url)']
    with open('./zhoushen_bilibili.csv', 'w', encoding='utf_8_sig', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(1, 5):
            r = requests.get(
                f'https://search.bilibili.com/all?keyword=%E5%91%A8%E6%B7%B1&page={i}', headers=ua)

            html = BeautifulSoup(r.text, 'html.parser')

            video_list = html.select('li.video-item.matrix')

            result = []

            for video in video_list:
                video_info = {}
                # 得到url
                url_element_get(video, video_info)

                play_count_element_get(video, video_info)

                danmu_element_get(video, video_info)

                upload_time_element(video, video_info)

                up_url_element_get(video, video_info)

                result.append(video_info)




        # header = ['题目(title)', '网址(url)', '播放量(play_count)', '弹幕(danmu)',
        #           '上传时间(upload_date)', '作者UP主(author)', 'UP主个人界面(author_url)']
        
        # with open('./zhoushen_bilibili.csv', 'w', encoding='utf_8_sig', newline='')as f:
        #     writer = csv.writer(f)
        #     writer.writerow(header)
        #     for i, element in enumerate(result):
        #         print(f'处理第{i + 1}条, 共{len(result)}条')
        #         row = element.values()
        #         print(row)
        #         writer.writerow(row)
        #         time.sleep(0.5)
    

            for i, element in enumerate(result):
                print(f'处理第{i + 1}条, 共{len(result)}条')
                row = element.values()
                print(row)
                writer.writerow(row)
                time.sleep(0.5)


if __name__ == '__main__':
    main()
