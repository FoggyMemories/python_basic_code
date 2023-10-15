"""
方法:
    列表的查询功能
    查找某元素的下标
    功能:查找指定元素再列表的下标,如果找不到,报错ValueError
    语法:列表.index(元素)
    index就是列表对象(变量)内置的方法(函数)
"""
my_list = ["123", 123, 123, 123, 123, 123, 12.3, True]
# 查询元素所在列表内的元素
print(my_list.index("123"))  # 查找的都是正向索引
print(my_list.index(123))
print(my_list.index(12.3))
print(my_list.index(True))
print(type(my_list.index(123)))  # int类型

# 统计某元素在列表内的数量
# 语法: 列表count(元素)
count = my_list.count(123)
print(count)

# 修改特定位置(索引)的元素值
# 语法:列表[索引] = 值  正反索引都可以
my_list[0] = "345"
my_list[-1] = False
for i in range(len(my_list)):
    print(f"{my_list[i]} ", end='')
print()
print(f"{my_list}")
print()

# 列表的插入
# 语法:列表.insert(下标, 元素)  :在指定的下标位置,插入指定的元素
my_list.insert(1, 'A')
for i in range(len(my_list)):
    print(f"{my_list[i]} ", end='')
print()
print(f"{my_list}")
print()

# 列表的删除
# 语法1: del 列表[索引]
# 语法2: 列表.pop(索引)
del my_list[1]  # del 没有返回值
index_1 = my_list.pop(1)
print(f"pop取出的元素是{index_1}")
for i in range(len(my_list)):
    print(f"{my_list[i]} ", end='')
print()
print(f"{my_list}")
print()

# 删除某元素在列表中的第一个匹配项
# 语法:列表.remove(元素)
index_2 = my_list.index(False)
remove = my_list.remove(False)
print(type(remove))
print(f"取出的元素是{remove},原本在list中的索引位置是{index_2}")
for i in range(len(my_list)):
    print(f"{my_list[i]} ", end='')
print()
print(f"{my_list}")
print()

# 追加元素:
# 语法"列表.append(元素),将指定元素,追加到列表的尾部
my_list.append(True)
for i in range(len(my_list)):
    print(f"{my_list[i]} ", end='')
print()
print(f"{my_list}")
print()

# 追加列表
# 语法:列表.extend(其他数据容器),将其他数据容器的内容取出,依次追加到列表尾部
my_list_2 = [123, 456, 789]
my_list.extend(my_list_2)  # 将另一个列表拼接在.前面的列表之中
for i in range(len(my_list)):
    print(f"{my_list[i]} ", end='')
print()
print(f"{my_list}")
for element in my_list:
    print(f"{element} ", end='')
print()

# 列表清空
# 语法: 列表.clear()
my_list.clear()
for i in range(len(my_list)):
    print(f"{my_list[i]} ", end='')
print()
print(f"{my_list}")
print()
