confession = 'Cyberpunk 2077, Hey Judy.'

# 初始化一个空字符串保存编码结果
message = ""

# 字符串是可迭代的，用 for 循环逐一取出单个字符
for char in confession:
    # 将字符传化为 ASCII 码表中对应的整数
    number = ord(char)
    # 再转化为十六进制字符串，比如 '0x97'
    hex_string = hex(number)
    # 通过切片去掉 '0x'，并追加到结果字符串尾部
    message += hex_string[2:]

print(message)