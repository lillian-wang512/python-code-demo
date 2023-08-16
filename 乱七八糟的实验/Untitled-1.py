import struct

tomato = "b'BM'"
tomato2 = "b'PK\\x03\\x04'"

# 使用 r 读取 b 二进制 模式打开文件
with open('你不看看我吗.bmp', 'rb') as f:
    # 读取 14 字节的文件头
    bmp_file_header = f.read(14)

    # BMP 文件头
    # bm 对应 2 字节的标志'BM'
    # size 对应 4 字节无符号整型表示文件大小
    # r1 r2 对应 2 个宽度为 2 字节的保留位置
    # offset 对应 4 字节无符号整型表示图像数据的起始偏移

    bm = struct.unpack('<2sIHHI', bmp_file_header)

    print(type(bm[0]))
    print(type(tomato))
    if str(bm[0])==tomato:
        print("ghj")


with open('考研讲义.pptx', 'rb') as f:
    # 读取 14 字节的文件头
    bmp_file_header = f.read(14)

    # BMP 文件头
    # bm 对应 2 字节的标志'BM'
    # size 对应 4 字节无符号整型表示文件大小
    # r1 r2 对应 2 个宽度为 2 字节的保留位置
    # offset 对应 4 字节无符号整型表示图像数据的起始偏移

    bm2 = struct.unpack('<2sIHHI', bmp_file_header)

    print(bm2[0])
    print(tomato2)

    if str(bm2[0])==tomato2:
        print("111")
