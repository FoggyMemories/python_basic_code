# 定义元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 不需要括号也可以
print(type(tup3))  # 查看类型

tup1 = ()  # 创建空元组
print(tup1)

# 元组中只包含一个元素时，需要在元素后面添加逗号 " , "，否则括号会被当作运算符使用
tup1 = (50)
print(type(tup1))  # 不加逗号，类型为整型

tup1 = (50,)
print(type(tup1))  # 加上逗号，类型为元组

# 访问元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 虽然不可以修改元组内的数据，但是如果元组内嵌套了一个list，就可以对list中的内容进行修改
t1 = (1, 2, ['test', 'hello'])
t1[2][1] = 'test1'
print(t1)  # (1, 2, ['test', 'test1'])

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组
tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup
print("删除后的元组 tup : ")
# print(tup)


# 元组索引，截取
tup = ('Google', 'Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
print(tup[1])
print(tup[-2])
print(tup[1:])
print(tup[1:4])
