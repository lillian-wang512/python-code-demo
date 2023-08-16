import requests
import csv
import os
import codecs
from bs4 import BeautifulSoup
allUniv = []


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)


def printUnivList(num):
    print("{:^4}{:^10}{:^5}{:^8}{:^10}".format(
        "排名", "学校名称", "省市", "总分", "培养规模"))
    for i in range(num):
        u[i] = allUniv[i]
        print("{:^4}{:^10}{:^5}{:^8}{:^10}".format(
            u[0], u[1], u[2], u[3], u[6]))


'''def write_csv_file(path, head, data):
    try:
        with open(path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
 
            if head is not None:
                writer.writerow(head)
 
            for row in data:
                writer.writerow(row)
 
            print("Write a CSV file to path %s Successful." % path)
    except Exception as e:
        print("Write an CSV file to path: %s, Case: %s" % (path, e))'''


def writercsv(save_road, num, title):
    if os.path.isfile(save_road):
        with open(save_road, 'a', newline='')as f:
            csv_write = csv.writer(f, dialect='excel')
            for i in range(num):
                u = allUniv[i]
                csv_write.writerow(u)
    else:
        with open(save_road, 'w', newline='')as f:
            csv_write = csv.writer(f, dialect='excel')
            csv_write.writerow(title)
            for i in range(num):
                u = allUniv[i]
                csv_write.writerow(u)


title = ["排名", "学校名称", "省市", "总分", "生源质量", "培养结果", "科研规模",
         "科研质量", "顶尖成果", "顶尖人才", "科技服务", "产学研究合作", "成果转化"]
save_road = "F:\\python\csvData.csv"


def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(10)
    writercsv('F:\\python\csvData.csv', 10, title)


if __name__ == '__main__':
    main()
# main()
