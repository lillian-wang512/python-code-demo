import requests
from bs4 import BeautifulSoup

ua = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

r = requests.get('https://search.bilibili.com/all?keyword=%E5%91%A8%E6%B7%B1', headers=ua)

html = BeautifulSoup(r.text, 'html.parser')

video_list = html.select('li.video-item.matrix')

print(video_list)

result = []
for video in video_list:
    video_info = {}

    url_element = video.select('div.info > div.headline.clearfix > a')
    video_info['title'] = url_element[0].text
    video_info['url'] = url_element[0]['href']

    play_count_element = video.select(
        'div.info > div.tags > span.watch-num')
    video_info['play_count'] = play_count_element[0].text.strip()

    danmu_element = video.select('div.info > div.tags > span.hide')
    video_info['danmu_count'] = danmu_element[0].text.strip()

    upload_time_element = video.select('div.info > div.tags > span.time')
    video_info['upload_date'] = upload_time_element[0].text.strip()

    up_url_element = video.select('div.info > div.tags > span > a.up-name')
    video_info['author'] = up_url_element[0].text
    video_info['author_url'] = up_url_element[0]['href']

    result.append(video_info)

print(result)