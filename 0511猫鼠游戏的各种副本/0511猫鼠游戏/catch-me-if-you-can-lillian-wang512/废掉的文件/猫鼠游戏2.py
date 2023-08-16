import struct
import os

# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符
def typeList():
    print('获取文件格式十六进制码表……')
    return {
        'ffd8ffe000104a464946':'jpg',
        '89504e470d0a1a0a0000':'png',
        '424d228c010000000000':'bmp',
        '424d8240090000000000':'bmp',
        '424d8e1b030000000000':'bmp',
        '255044462d312e350d0a':'pdf',
        '504b0304140006000800':'docx',
        '4d5a9000030000000400':'exe',
        }
 
 
# 字节码转16进制字符串
def bytes2hex(bytes):
    print('关键码转码……')
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
    print('读文件二进制码中……')
    binfile = open(filename, 'rb') # 必需二制字读取
    print('提取关键码……')
    print("1") #测试一下
    bins = binfile.read(20) #提取20个字符
    binfile.close() #关闭文件流
    bins = bytes2hex(bins) #转码
    bins = bins.lower()#小写
    print(bins)
    tl = typeList() #文件类型
    ftype = 'unknown'
    print('关键码比对中……')
    for hcode in tl.keys():
        lens = len(hcode) # 需要的长度
        if bins[0:lens] == hcode:
            ftype = tl[hcode]
            break
    if ftype == 'unknown':#全码未找到，优化处理，码表取5位验证
        bins = bins[0:5]
        for hcode in tl.keys():
            if len(hcode) > 5 and bins == hcode[0:5]:
                ftype = tl[hcode]
                break
    return ftype
 
 
#文件扫描，如果是目录，就将遍历文件，是文件就判断文件类型
def filescanner(path):
    if type(path) != type('a'):#判断是否为字符串
        print('抱歉，你输入的不是一个字符串路径！')
    elif path.strip() == '':#将两头的空格移除
        print('输入的路径为空！')
    elif not os.path.exists(path):
        print('输入的路径不存在！')
    elif os.path.isfile(path):
        print('输入的路径指向的是文件，验证文件类型……')
        if path.rfind('.') > 0:
            print('文件名:',os.path.split(path)[1])
            print("111")
        else:
            print('文件名中没有找到格式')
        path = filetype(path)
        print('解析文件判断格式：'+path)
    elif os.path.isdir(path):
        print('输入的路径指向的是目录，开始遍历文件')
        for p,d,fs in os.walk(path):
            print(os.path.split(p))
            for n in fs:
                n=n.split('.')
                print('\t'+n[0]+'\t'+n[1])
                
if __name__ == '__main__':
    #print('WinSonZhao，欢迎你使用文件扫描工具……')
    path=input('请输入要扫描的文件夹路径：')
    filescanner(path)
    print('扫描结束！')



# 按文件大小由大到小命名的新目录
output_dir1 = "D:\安靖Python\\0511猫鼠游戏\catch-me-if-you-can-lillian-wang512\正常"
output_dir2 = "D:\安靖Python\\0511猫鼠游戏\catch-me-if-you-can-lillian-wang512\异常"


 # 调用 os.rename() 实现移动文件的效果
if path != :
    os.rename(file, output_dir1)
else:
    os.rename(file, output_dir2)
   
