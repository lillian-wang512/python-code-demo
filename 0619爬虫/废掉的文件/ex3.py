import requests
from bs4 import BeautifulSoup
import json
import csv
import codecs


def get_city_aqi(pinyin):
    url = 'http://www.pm25.in/' + pinyin
    r = requests.get(url, timeout=60)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        # city_aqi.append((caption, value))
        city_aqi.append(value)
    return city_aqi


def get_all_cities():
    url = 'http://www.pm25.in/'
    city_list = []
    r = requests.get(url, timeout=60)
    soup = BeautifulSoup(r.text, 'lxml')
    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    city_list = get_all_cities()
    #print(city_list)
    header = ['City', 'AQI', 'PM2.5/h', 'PM10/h', 'CO/h', 'NO2/h', 'O3/h', 'O3/8h', 'SO2/h']
    with open('./china_city_aqi4.csv', 'w', encoding='utf_8_sig', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            #print(type(city))
            #print("111111111111")
            print(f'处理第{i + 1}条, 共{len(city_list)}条')
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            print(row)
            writer.writerow(row)


if __name__ == '__main__':
    main()
