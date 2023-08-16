# 列表

# 增加內容
# 列表相加
# a = [1, 2, 3]
# b = [4, 5, 6]
# a +=
# print(a)  # [1, 2, 3, 4, 5, 6]

# 列表數乘
# a = [1, 2, 3]
# a *= 3
# print(a)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 列表append,extend
# a = [1, 2, 3, 4]
# a.append(10)
# print(a)  # [1, 2, 3, 4, 10]
# a.append([1, 2])
# print(a)  # [1, 2, 3, 4, 10, [1, 2]]
# a.clear()  # 清空列表
# a.extend([1, 2, 3])
# print(a)  # [1, 2, 3]
# a.extend((7, 8, 9))  # 插入元組
# print(a)  # [1, 2, 3, 7, 8, 9]

# 列表插入insert
# a = [1, 2, 3, 4]
# a.insert(3, 11)  # 在索引為三的位置插入11這個數字
# print(a)  # [1, 2, 3, 11, 4]
# a.insert(0, 0)
# print(a)  # [0, 1, 2, 3, 11, 4]
# a.insert(0, 'a')
# print(a)  # ['a', 0, 1, 2, 3, 11, 4]


# 更新內容
# 切片替換
# a = [x for x in range(10)]
# a[2:5] = [115]  # 切片取左不取右
# print(a)  # [0, 1, 115, 5, 6, 7, 8, 9]

# a = [x for x in range(10)]
# a[0::2] = ['a', 'b', 'c', 'd', 'e']  # 左右替換長度严格相等
# print(a)  # ['a', 1, 'b', 3, 'c', 5, 'd', 7, 'e', 9]

# 排序
# a = [10, 4, 6, 2, 55, 41, 33, 5]
# a.sort()  # 只改变a本身
# d = a.sort()
# print(a)  # [2, 4, 5, 6, 10, 33, 41, 55]
# print(d)  # None
# # 反转列表排序
# a.reverse()
# print(a)  # [55, 41, 33, 10, 6, 5, 4, 2]


# 查找内容：in和not in
# a = ['罗翔', '作业', 'anjing', 'c++', '放假', '罗翔']
# if 'python' in a:
#     print("泪目了")
# elif '放假' in a:
#     print('芜湖起飞')
# else:
#     print('难过www')
# # 结果：芜湖起飞

# # 最大值最小值：min(a),max(a)
# # index：查找并返回第一次出现的位置
# print(a.index('anjing')+1)  # 3
# # count：一个元素在列表中出现了多少次
# print(a.count('罗翔'))  # 2


# # 元组中可以只有一项内容，单独使用元组时括号可以省略，但逗号是不能省略的
# teachers = 'anjing',

# # 元组支持拼接操作
# more_teachers = teachers + ('Tom', 'Jerry')

# # 支持全切片复制元组，但不支持 .copy()
# same_teachers = more_teachers[:]

# # 支持查找，但不支持排序 .sort()
# same_teachers.index('anjing')

# # 支持哈希
# print(hash(same_teachers))

# 可以整体删除但不支持部分删除
# del more_teachers
# del teachers

# 集合可以去重
# a = ['罗翔', '作业', 'anjing', 'c++', '放假', '罗翔']

# b = list(set(a))

# print(b)


# 字典

# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}  # 最常用
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# d = dict([('two', 2), ('one', 1), ('three', 3)])
# e = dict({'three': 3, 'one': 1, 'two': 2})

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#结果
# {'one': 1, 'two': 2, 'three': 3}
# {'one': 1, 'two': 2, 'three': 3}
# {'one': 1, 'two': 2, 'three': 3}
# {'two': 2, 'one': 1, 'three': 3}
# {'three': 3, 'one': 1, 'two': 2}

#冒号前面的是key,后面的是value
