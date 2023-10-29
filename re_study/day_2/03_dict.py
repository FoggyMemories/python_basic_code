# 定义字典
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}

# 创建空字典
# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

# 使用内建函数 dict() 创建字典
emptyDict = dict()

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

# 访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# 修改字典
tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 删除字典元素
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典

# print("tinydict['Age']: ", tinydict['Age'])
# print("tinydict['School']: ", tinydict['School'])
# 因为用执行 del 操作后字典不再存在,会引发一个异常

# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("tinydict['Name']: ", tinydict['Name'])


# 键必须不可变，所以可以用数字，字符串或元组充当，而使用列表不行
# tinydict = {['Name']: 'Runoob', 'Age': 7}

# print("tinydict['Name']: ", tinydict['Name'])
