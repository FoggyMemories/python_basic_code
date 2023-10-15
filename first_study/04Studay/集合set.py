"""
集合的定义
    基本语法:
        变量名称 = {元素,元素,元素,...,元素}
    定义空集合:
        变量名称 = set()
和列表、元素、字符串等定义基本相同
* 列表使用：[]
* 元组使用: ()
* 字符串使用: ""

"""

my_set = {"123", "321", 123, 12.3, True, -321, 'a'}
my_set_empty = set()
print(my_set, type(my_set))  # 去重,乱序,集合是不允许重复的
# 集合不支持通过索引进行访问

my_set.add("456")
print(my_set)

my_set.remove("123")
print(my_set)

# 从集合中随机抽取元素
# 语法： 集合.pop()  由于集合中没有索引的说法,所以说,取出来的是随机的
element = my_set.pop()
print(my_set)
print(element)

# 清空元素
my_set.clear()
print(my_set)

# 取出2个集合的差集
# 语法: 集合1.difference(集合2)       功能: 取出集合1和集合2的差集(集合1有而集合2没有的)
# 具有返回值:得到一个新集合,集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set3)  # 集合1有,但是集合2没有
print(set1)
print(set2)

# 消除2个集合的差集
# 语法:集合1.difference_update(集合2)     功能:对比集合1和集合2,在集合1内,删除和集合2相同的元素
# 结果:集合1被修改,集合2不变,没有返回值
set1.difference_update(set2)
print(set1)  # 只修改set1内部与set2重复的值
print(set2)

set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 两个集合的合并
# 语法: 集合.union(集合)
# 有返回值,不会对原集合进行修改
print(set1.union(set2))  # 不能对自身进行合并,由于集合的特性,会进行去重处理

"""
总结:
    1.如果集合的元素都是数字,删除时,删掉的是最小的数字,其余数字升序排列
    2.如果集合的元素是非数字,删除时,删掉的是随机的元素,其余元素随机排列
    3.如果集合里既有数字又有非数字元素,删除时:
        若删掉的是数字,则一定是删掉了最小的,其他数字升序排列,非数字元素随机排列
        若删掉的是非数字,则一定是最忌删掉一个,其他数字升序排列,非数字则随机排列
"""
print()
print()
print()
print()
print()
set_test = {1, 2, 3, 4, 5, 6}
print(set_test.pop())

for i in set_test:
    print(i, end='')
set_test.clear()
print()
print(set_test)

set_test_2 = {"123", "123", "123", "123", "456"}
my_set_input = set()
for i in set_test_2:
    my_set_input.add(i)
print(my_set_input)
