# 切片：从一个序列中，取出一个子序列
# 语法：序列[其实索引:结束索引:步长]
# 包头包尾
my_list = [0, 1, 2, 3, 4, 5, 6]
result = my_list[1:4]  # 默认步长为1,所以可以省略不写
print(result, type(result))

my_tuple = ("123", True, 123, 12.3, 'A')

print(my_tuple[:])  # 从头到尾,步长默认为1

print(my_tuple[1:4:2], type(my_tuple))  # 步长为2
print(my_tuple[-1:-(len(my_tuple) + 1):-1])
print(my_tuple[::-1])  # 同样是从后向前进行排序

test_str = "万过薪月,员序程睿钱来,nohtyP学"
print(test_str[-9: -14: -1])
re_test_str = test_str[::-1]
print(re_test_str)
print(re_test_str[9:14])
for i in range(len(re_test_str)):
    if (i >= 9) & (i < 14):
        print(re_test_str[i], end='')

print()
print(re_test_str.split(",")[1].replace("来", ""))
