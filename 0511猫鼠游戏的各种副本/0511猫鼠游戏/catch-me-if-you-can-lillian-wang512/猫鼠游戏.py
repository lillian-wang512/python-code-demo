import struct
import os


# 通过递归调用 os.listdir() 来实现目录遍历，得到一个包含所有文件的列表
def walk_dir(path):
    result = []

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isdir(file_path):
            result += walk_dir(file_path)

        if os.path.isfile(file_path):
            result.append(file_path)

    return result


root = input('请输入你要遍历的目录: ')

# 遍历用户指定的目录
files = walk_dir(root)

# 按文件大小由大到小命名的新目录
output_dir = input('请输入你要新建的目录: ')

# 新目录不存在时自动创建这个目录
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# 使用 os.stat() 获取文件大小
file_dict = {}
for file in files:
    st = os.stat(file)
    file_dict[file] = st.st_size

# 用 数据类型进阶 一节学过的方法排序
sorted_files = {
    k: v
    for k, v in sorted(file_dict.items(), key=lambda x: x[1], reverse=True)
}

# 按照由大到小的顺序，给文件名前面加上数字前缀并移动到新的目录
filename = 1
for file in sorted_files.keys():
    # 获取文件名的部分（不包括前面的路径）
    basename = os.path.basename(file)
    # 将文件名拆分成名字和后缀
    name, ext = os.path.splitext(basename)

if __name__ == "__main__":
    rootdir = '.\CatchMeIfYouCan'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        # if os.path.isfile(path):
        # # 你想对文件的操作
        print(path)


        # 使用 r 读取 b 二进制 模式打开文件
        with open(basename, 'rb') as f:
        # 读取 14 字节的文件头
            bmp_file_header = f.read(14)

        # BMP 文件头
        # bm 对应 2 字节的标志'BM'

            bm = struct.unpack('<2sIHHI', bmp_file_header)

            print(bm[0])

        if bm[0] == "b'BM'":

            # 组合新的目录和新文件名
            new_basename=basename
            # new_basename = str(filename) + '_' + name + ext
            newfilename = os.path.join(output_dir, new_basename)

            # 调用 os.rename() 实现移动文件的效果
            os.rename(file, newfilename)

            # filename += 1
       


