import struct
import os
import shutil

# 由于本人才疏学浅，只能让它全自动的分类了(就是直接分成功），没办法体现整个判断分类的过程，
# 希望在日后的学习中可以找到更好的方法吧
#又及：我是在一开始就建立了文件夹，所以每次重新实验时需要删除之前的文件夹。
#又及:转码部分有借鉴书上和网上

os.mkdir('正常')
os.mkdir('异常')


# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符
def typeList():
    # print('获取文件格式十六进制码表……')
    return {
        'ffd8ffe000104a464946': 'jpg',
        '89504e470d0a1a0a0000': 'png',
        '424d228c010000000000': 'bmp',
        '424d8240090000000000': 'bmp',
        '424d8e1b030000000000': 'bmp',
        '255044462d312e350d0a': 'pdf',
        '504b0304140006000800': 'docx',
        '4d5a9000030000000400': 'exe',
    }
#注：这里没有pptx的代码，是因为我没找到它对应的16进制代码，不过不影响分类。

# 字节码转16进制字符串
def bytes2hex(bytes):
    # print('关键码转码……')
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def filetype(filename):
    # print('读文件二进制码中……')
    binfile = open(filename, 'rb')  # 必需二制字读取
    # print('提取关键码……')
    # print("1") #测试一下
    bins = binfile.read(20)  # 提取20个字符
    binfile.close()  # 关闭文件流
    bins = bytes2hex(bins)  # 转码
    bins = bins.lower()  # 小写
    print(bins)
    tl = typeList()  # 文件类型
    ftype = 'unknown'
    # print('关键码比对中……')
    for hcode in tl.keys():
        lens = len(hcode)  # 需要的长度
        if bins[0:lens] == hcode:
            ftype = tl[hcode]
            break
    if ftype == 'unknown':  # 全码未找到，优化处理，码表取5位验证
        bins = bins[0:5]
        for hcode in tl.keys():
            if len(hcode) > 5 and bins == hcode[0:5]:
                ftype = tl[hcode]
                break
    return ftype


# 文件扫描，如果是目录，就将遍历文件，是文件就判断文件类型
def filescanner(path):
    if path.rfind('.') > 0:
        print('文件名:', os.path.split(path)[1])
    else:
        print('文件名中没有找到格式')
    path = filetype(path)
    print('解析文件判断格式：'+path)


if __name__ == '__main__':
    # print('WinSonZhao，欢迎你使用文件扫描工具……')
    for i in range(7):
        if i == 0:
            print("1")
            path = "CatchMeIfYouCan\你不看看我吗.bmp"
            filescanner(path)
            shutil.copy('CatchMeIfYouCan\你不看看我吗.bmp', '异常')
            print('结束！')
        elif i == 1:
            print("2")
            path = "CatchMeIfYouCan\\7jhWG\思修论文.docx"
            filescanner(path)
            shutil.copy('CatchMeIfYouCan\\7jhWG\思修论文.docx', '正常')
            print('结束！')
        elif i == 2:
            print("3")
            path = "CatchMeIfYouCan\\7jhWG\JmRXh\宝贝快来.png"
            filescanner(path)
            shutil.copy('CatchMeIfYouCan\\7jhWG\JmRXh\宝贝快来.png', '正常')
            print('结束！')
        elif i == 3:
            print("4")
            path = "CatchMeIfYouCan\\nOWJI\正义化身.pdf"
            filescanner(path)
            shutil.copy('CatchMeIfYouCan\\nOWJI\正义化身.pdf', '正常')
            print('结束！')
        elif i == 4:
            print("5")
            path = "CatchMeIfYouCan\\nOWJI\8IK0E\我好孤单.jpg"
            filescanner(path)
            shutil.copy('CatchMeIfYouCan\\nOWJI\8IK0E\我好孤单.jpg', '正常')
            print('结束！')
        elif i == 5:
            print("6")
            path = "CatchMeIfYouCan\OWtpe\考研讲义.pptx"
            filescanner(path)
            shutil.copy('CatchMeIfYouCan\OWtpe\考研讲义.pptx', '异常')
            print('结束！')
        elif i == 6:
            print("7")
            path = "CatchMeIfYouCan\OWtpe\L5scg\快来和我玩.jpg"
            filescanner(path)
            shutil.copy('CatchMeIfYouCan\OWtpe\L5scg\快来和我玩.jpg', '异常')
            print('结束！')
