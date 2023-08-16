# # 字符转base64编码

# # 我把编码和解码写在同一个文件里了，不过它也可以分开使用，只是不想把它分开了，详情（代码运行情况）请见我的传上去的.md文件

# # confession="Man"      #输入字符
# import time  # 时间模块
# confession = input("请输入字符：")
# group_string = ''       # 设置空字符串(中间没有空格，否则最终的字符串也有空格)
# base64_string = ""
# group_string2 = ''
# count2 = 0

# # base64类型码
# base_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# # 复制一下，以后要用
# confession_copy = confession
# # 按顺序选出三个字符进行转码
# for char2 in range(0, len(confession)):
#     # 将每一个字符转为二进制
#     group = confession[:1]  # 选出第一个字符进行转码
#     asc = bin(ord(group))  # 转为二进制（字符转整数，再转二进制）
#     asc = str(asc)  # 二进制转为字符串形式（便于之后查找）
#     # 将二进制符开头的"0b"删除，改为"0"(就是改成8个bit的二进制)

#     asc = asc[2:]
#     if len(asc) < 8:
#         count = 8-len(asc)
#         # 补0
#         for i in range(count):
#             asc = "0"+asc   
#     group_string = group_string+asc  
#     # group_string = group_string+"0"+asc[2:]

#     confession = confession[1:]  # 去除第一个字符，下次将运行第二个字符

# # 判断字符数是否是三的倍数，从而断定要添加几个零

# # if len(confession_copy) % 3 != 0:
# #     for i in range(0, 3-len(confession_copy) % 3):
# #         group_string += "00"

# # 每6个二进制bit转成十进制整数
# for char in range(0, len(group_string), 6):
#     int_num = int(group_string[char:char+6], 2)  # 6个二进制符转整数
#     base64_string += base_string[int_num]   # 按照整数在64进制里查找

# # 判断字符数是否是三的倍数，从而断定要在base64编码中添加几个"="
# if len(confession_copy) % 3 != 0:
#     for i in range(0, 3-len(confession_copy) % 3):
#         base64_string += "="   


# print(" ")  # 没别的，打印出来好看
# print("该字符的base64编码为:"+base64_string)  # 打印base64编码

# time.sleep(1)  # 为了好看，1 second


# # base64转字符串
# # 例子：TWFu

# # 先定义一下
# count = 0
# confession_string2 = ""
# base2_string2 = ""

# print(" ")  # 好看
# base64_string = input("请输入base64编码：")  # 输入base64编码

# # 判断base64编码中有没有"=",有则删除
# for char6 in range(0, len(base64_string)):
#     if base64_string[char6] == "=":
#         base64_string = base64_string[:char6]
#         break

# # 转码，转回去
# for char5 in range(0, len(base64_string)):
#     # 在base64_string中查找对应的位置
#     base10_string = base_string.index(base64_string[char5])
#     # 十进制转二进制
#     base2_string = bin(base10_string)
#     # 将0b切片
#     base2_string = base2_string[2:]
#     # 判断是否满足6位，不足补齐
#     if len(base2_string) < 6:
#         count = 6-len(base2_string)
#         # 补0
#         for i in range(0, count):
#             base2_string = "0"+base2_string
#     # 用一个空字符串进行存储
#     base2_string2 += base2_string

# # 转换成的二进制字符串每八位转十进制
# for char4 in range(0, len(base2_string2), 8):
#     group2_string = int(base2_string2[0:8], 2)
#     # 十进制转字符（ascii）
#     confession_string = chr(group2_string)
#     confession_string2 += confession_string  # 存储
#     base2_string2 = base2_string2[8:]  # 切片，下一个

# print(" ")  # 纯粹为了好看233
# print("解码："+confession_string2)  # 输出解码


# # 布尔逻辑
# 真值检测：判断为假的条件：1.None和False
#                       2.0,0.0,0j
#                       3.空的序列和多项集："",(),[],range(0)

# x = 10
# y = 100

# if (x > 50) and (y > 100):
#     print("demo")
# else:
#     print("no")

# if 'A'>'B':    #ascii表
#     print('true')
# else:
#     print('false')


# while循环

# numbers = [12, 37, 5, 42, 8, 3]
# even = []
# odd = []

# while len(numbers) > 0:
#     number = numbers.pop()
#     if (number % 2 == 0):
#         even.append(number)
#         print('even='+ str(even))
#     else:
#         odd.append(number)
#         print('odd='+str(odd))


# for循环

# for char in 'python':
#     print(char)  # p,y,t,h,o,n

# for i in [1, 2, 3]:
#     print(i)  # 1,2,3

# for i in (1, 2, 3):
#     print(i)  # 1,2,3

# for i in range(8):
#     print(i)  # 0,1,2,3,4,5,6,7

# for i in range(0, 10):
#     print(i)  # 0,1,2,3,4,5,6,7,8,9

# for i in range(0, 10, 2):
#     print(i)  # 0,2,4,6,8

# a = [x for x in range(0, 6, 2)]  #存在列表里
# print(a)


# 函数
# def sum(a, b):
#     c = a + b
#     return c

# print(sum(1, 2))


# 倒数
# def countdown(start=10):
#     while start:
#         start -= 1
#         print(start)


# if __name__ == "__main__":
#     countdown()
#     countdown(100)
#     countdown(start=5)


# 参数名前用*，则可以使用（传进来）任意个数的参数
# 加*的东西会被当成元组来对待

# def concat(*args, sep=' '):
#     print(type(args))
#     return sep.join(args)


# print(concat('abc', 'def'))  # 'abc  def'


# 匿名函数Lambda
# pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
# pairs.sort(key=lambda p:p[1])
# print(pairs)

# #函数形式
# def get_second_item(p):
#     return p[1]

# pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
# pairs.sort(key=get_second_item)
# print(pairs)



# # 字符转base64编码

# #我把编码和解码写在同一个文件里了，不过它也可以分开使用，只是不想把它分开了，详情（代码运行情况）请见我的传上去的.md文件

# # confession="Man"      #输入字符
# import time  # 时间模块
# confession = input("请输入字符：")
# group_string = ''       # 设置空字符串(中间没有空格，否则最终的字符串也有空格)
# base64_string = ""
# count2 = 0

# # base64类型码
# base_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# # 复制一下，以后要用
# confession_copy = confession
# # 按顺序选出三个字符进行转码
# for char2 in range(0, len(confession)):
#     # 将每一个字符转为二进制
#     group = confession[:1]  # 选出第一个字符进行转码
#     asc = bin(ord(group))  # 转为二进制（字符转整数，再转二进制）
#     asc = str(asc)  # 二进制转为字符串形式（便于之后查找）
#     # 将二进制符开头的"0b"删除，改为"0"(就是改成8个bit的二进制)
#     group_string = group_string+"0"+asc[2:]

#     confession = confession[1:]  # 去除第一个字符，下次将运行第二个字符

# # 判断字符数是否是三的倍数，从而断定要添加几个零
# if len(confession_copy) % 3 != 0:
#     for i in range(0, 3-len(confession_copy) % 3):
#         group_string += "00"

# # 每6个二进制bit转成十进制整数
# for char in range(0, len(group_string), 6):
#     int_num = int(group_string[char:char+6], 2)  # 6个二进制符转整数
#     base64_string += base_string[int_num]   # 按照整数在64进制里查找

# # 判断字符数是否是三的倍数，从而断定要在base64编码中添加几个"="
# if len(confession_copy) % 3 != 0:
#     for i in range(0, 3-len(confession_copy) % 3):
#         base64_string += "="


# print(" ")  # 没别的，打印出来好看
# print("该字符的base64编码为:"+base64_string)  # 打印base64编码

# time.sleep(1)  # 为了好看，1 second


# # base64转字符串
# # 例子：TWFu

# # 先定义一下
# count = 0
# confession_string2 = ""
# base2_string2 = ""

# print(" ")  # 好看
# base64_string = input("请输入base64编码：")  # 输入base64编码

# # 判断base64编码中有没有"=",有则删除
# for char6 in range(0, len(base64_string)):
#     if base64_string[char6] == "=":
#         base64_string = base64_string[:char6]
#         break

# # 转码，转回去
# for char5 in range(0, len(base64_string)):
#     # 在base64_string中查找对应的位置
#     base10_string = base_string.index(base64_string[char5])
#     # 十进制转二进制
#     base2_string = bin(base10_string)
#     # 将0b切片
#     base2_string = base2_string[2:]
#     # 判断是否满足6位，不足补齐
#     if len(base2_string) < 6:
#         count = 6-len(base2_string)
#         # 补0
#         for i in range(0, count):
#             base2_string = "0"+base2_string
#     # 用一个空字符串进行存储
#     base2_string2 += base2_string

# # 转换成的二进制字符串每八位转十进制
# for char4 in range(0, len(base2_string2), 8):
#     group2_string = int(base2_string2[0:8], 2)
#     # 十进制转字符（ascii）
#     confession_string = chr(group2_string)
#     confession_string2 += confession_string  # 存储
#     base2_string2 = base2_string2[8:]  # 切片，下一个

# print(" ")  # 纯粹为了好看233
# print("解码："+confession_string2)  # 输出解码


# 字符转base64编码

# 我把编码和解码写在同一个文件里了，不过它也可以分开使用，只是不想把它分开了，详情（代码运行情况）请见我的传上去的.md文件

# confession="Man"      #输入字符
import time  # 时间模块
confession = input("请输入字符：")
group_string = ''       # 设置空字符串(中间没有空格，否则最终的字符串也有空格)
base64_string = ""
group_string2 = ''
count2 = 0

# base64类型码
base_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# 复制一下，以后要用
confession_copy = confession
# 按顺序选出三个字符进行转码
for char2 in range(0, len(confession)):
    # 将每一个字符转为二进制
    group = confession[:1]  # 选出第一个字符进行转码
    asc = bin(ord(group))  # 转为二进制（字符转整数，再转二进制）
    asc = str(asc)  # 二进制转为字符串形式（便于之后查找）
    # 将二进制符开头的"0b"删除，改为"0"(就是改成8个bit的二进制)

    asc = asc[2:]
    if len(asc) < 8:
        count = 8-len(asc)
        # 补0
        for i in range(count):
            asc = "0"+asc   
    group_string = group_string+asc  
    # group_string = group_string+"0"+asc[2:]

    confession = confession[1:]  # 去除第一个字符，下次将运行第二个字符

# 判断字符数是否是三的倍数，从而断定要添加几个零

# if len(confession_copy) % 3 != 0:
#     for i in range(0, 3-len(confession_copy) % 3):
#         group_string += "00"

# 每6个二进制bit转成十进制整数
for char in range(0, len(group_string), 6):
    int_num = int(group_string[char:char+6], 2)  # 6个二进制符转整数
    base64_string += base_string[int_num]   # 按照整数在64进制里查找

# 判断字符数是否是三的倍数，从而断定要在base64编码中添加几个"="
if len(confession_copy) % 3 != 0:
    for i in range(0, 3-len(confession_copy) % 3):
        base64_string += "="   


print(" ")  # 没别的，打印出来好看
print("该字符的base64编码为:"+base64_string)  # 打印base64编码

time.sleep(1)  # 为了好看，1 second


# base64转字符串
# 例子：TWFu

# 先定义一下
count = 0
confession_string2 = ""
base2_string2 = ""

print(" ")  # 好看
base64_string = input("请输入base64编码：")  # 输入base64编码

# 判断base64编码中有没有"=",有则删除
for char6 in range(0, len(base64_string)):
    if base64_string[char6] == "=":
        base64_string = base64_string[:char6]
        break

# 转码，转回去
for char5 in range(0, len(base64_string)):
    # 在base64_string中查找对应的位置
    base10_string = base_string.index(base64_string[char5])
    # 十进制转二进制
    base2_string = bin(base10_string)
    # 将0b切片
    base2_string = base2_string[2:]
    # 判断是否满足6位，不足补齐
    if len(base2_string) < 6:
        count = 6-len(base2_string)
        # 补0
        for i in range(0, count):
            base2_string = "0"+base2_string
    # 用一个空字符串进行存储
    base2_string2 += base2_string

# 转换成的二进制字符串每八位转十进制
for char4 in range(0, len(base2_string2), 8):
    group2_string = int(base2_string2[0:8], 2)
    # 十进制转字符（ascii）
    confession_string = chr(group2_string)
    confession_string2 += confession_string  # 存储
    base2_string2 = base2_string2[8:]  # 切片，下一个

print(" ")  # 纯粹为了好看233
print("解码："+confession_string2)  # 输出解码
