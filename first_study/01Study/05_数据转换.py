"""
万物皆可转化为字符串
"""

# 将int类型转化为 字符串类型
num_str = str(11)
print(type(num_str), num_str)

# 将字符串类型转化为 整数类型
num = int("11")
print(type(num), num)

# 将字符串类型转化为 小数类型
num2 = float("11.345")
print(type(num2), num2)

# 将字符串转化为 整数类型 此时会报错,转化失败
# 只有字符串中的内容全为数字的情况下才能转化为 整数或者其他类型
"""
num3 = int("钱睿")
print(type(num3), num3)
"""

num3 = int("123")
print(type(num3), num3)

float_num = float(11)
print(type(float_num), float_num)

int_num = int(11.345)
print(type(int_num), int_num)
