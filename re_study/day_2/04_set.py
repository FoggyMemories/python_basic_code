# 集合（set）是一个无序的不重复元素序列。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

# 定义集合
set1 = {1, 2, 3, 4}  # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])  # 使用 set() 函数从列表创建集合

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能

# 两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(f"{a-b=}")
print(f"{a|b=}")
print(f"{a&b=}")
print(f"{a^b=}")

# 集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 添加元素
thisset = {"Google", "Runoob", "Taobao"}
thisset.add("Facebook")
print(thisset)

# 另一种方法也可以添加元素，且参数可以是列表，元组，字典等
thisset = {"Google", "Runoob", "Taobao"}
thisset.update({1, 3})
print(thisset)

# 移除元素
# 当移除的元素不存在时会发生错误
thisset.remove("Taobao")
print(thisset)

# 不存在不会发生错误
thisset.discard("Facebook")
print(thisset)

# 设置随机删除集合中的一个元素
x = thisset.pop()
print(x)
print(thisset)

# 清空集合
thisset.clear()
print(thisset)

# 判断元素是否在集合中存在
thisset = {"Google", "Runoob", "Taobao"}
print("Runoob" in thisset)  # True
