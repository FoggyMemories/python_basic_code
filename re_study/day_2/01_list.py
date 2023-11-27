# 定义列表
my_list = ["test", True, 1]
print(my_list)
test = []
print(test)

# 定义嵌套列表
my_list = [[1, 2, 3], [1, 2, 3]]
print(my_list)

# 实例
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[0])
print(list[1])
print(list[2])

list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[-1])
print(list[-2])
print(list[-3])

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])

list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# 列表的查询
print(list.index('Google'))  # 0

# 读取第二位
print("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print("list[1:-2]: ", list[1:-2])

# 列表的追加
list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print("更新后的列表 : ", list1)

# 列表的插入(在指定下标位置插入新元素)
list1.insert(1, 'best')
print(f"列表插入元素后输出结果是:{list1}")

# 删除列表元素
list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)
print(f"通过pop方法取出的元素为：{list.pop(2)},后列表为：{list}")

# 删除某元素在列表中的第一个匹配项
list = ['1', '2', '3', '1', '4']
list.remove('1')
print(f"通过remove方法移除元素后，列表的结果是：{list}")

# 清空列表
list.clear()
print(f"列表清空了，结果是{list}")

# 列表的截取与拼接
L = ['Google', 'Runoob', 'Taobao']
print(L[2])

squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)

# 统计某元素在列表内的数量
print(f"\"1\"在列表中出现的次数为:{squares.count(1)}")

# 列表的嵌套
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][1])

# 列表嵌套的时候只能查询一维列表在二位数组中的索引,并不能查询元素在二维列表中的索引
print(x.index(a))