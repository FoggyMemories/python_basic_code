# 字典的定义
# 同样使用{}，不过存储的元素是一个个的： 键值对
# 语法：   变量 = {kay: value,key: value,....,key: value}
# 定义空字典：    变量 = {}  、  变量 = dict()

my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# 构建新的空字典
my_dict_2 = dict()
my_dict_3 = {}
# key不允许重复  key同样的没有索引的说法
print(my_dict)
print(type(my_dict))


# 字典数据的获取
# 语法： 字典[key]可以取到对应的Value
print(my_dict[1])   # 输入的是key,返回的是Value
