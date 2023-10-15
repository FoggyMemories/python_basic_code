# 同样的,可以理解为字符串是一个容器,索引 功能同样使用
my_str = "asdfghjklp and\a zxcvbnm"
index_2 = my_str[2]
print(index_2)
index_10 = my_str[10]
print(index_10)  # 任意符号在之中都可以打印
index_14 = my_str[14]
index_15 = my_str[15]
print(index_14, "\n", index_15)  # 此时\a转义,占一个索引

value = my_str.index("and")
print(value)  # 计算的是这个小字符串的首字符在字符串中的索引位


#
#
#
# 字符串的替换
replace_str = my_str.replace("and", "or")  # .replace具有返回值,生成一个新的str变量
print(replace_str)  # .replace替换字符串 所有的字符,无论索引在前还是在后

# 字符串的分割
# 语法: 字符串.split(分隔符字符串)
# 功能: 按照指定的分隔符字符串,将字符串划分为多个字符串,并存入列表对象中
# 注意: 字符串本身不变,而是得到了一个列表对象
my_str_list = my_str.split(" ")
print(my_str_list, type(my_str_list))  # 将之前的字符串按照" "的形式切分成一个列表

# 字符串的规整操作(去前后空格)
# 语法: 字符串.strip()
my_str = "   new test one String  !    "
print(my_str.strip())  # 不传入参数的情况下,是去除头和尾部的空格

# 字符串的规整操作(取出前后指定的字符串)
# 语法: 字符串.strip(字符串)
print(my_str.strip(" "))  # 传入的字符前后没有顺序之分,移除得得是其中的单个字符串
str_test = "123 test 321"
print(str_test.strip("23t1"))  # 无前后顺序之分 且不包括空格,分别从两边向中间查询,都查询不到的时候暂停查询

print(str_test.count(" "))

for i in my_str:
    print(i, end='')
