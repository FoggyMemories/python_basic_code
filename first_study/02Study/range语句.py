# 学习range语句,获得一个简单的数字序列.

# 语法1:
"""
range(num)
获取一个从0开始,到num结束的数字序列,包头不包尾
如range(5)获得的数据是:[0, 1, 2, 3, 4]
"""
# 语法2
"""
range(num1, num2)
获得一个从num1开始到num2的数字,包头不包尾
如,range(5, 10)取得的数字是:[5, 6, 7, 8, 9]
"""

# 语法3
"""
range(num1, num2, step)
获得一个从num1开始,到num2结束的数字序列,包头不包尾
数字之间的步长,以step为准(step默认为1)
如,range(5, 10, 2)取得的数据是:[5, 7, 9]
"""

for x in range(10):
    print(x, end='')

print()

for x in range(2, 10):
    print(x, end='')

print()

for x in range(2, 10, 2):
    print(x, end='')

print()

for x in range(10):
    print("运行的第%d次" % (x + 1))

count = 0
# 查询有多少个偶数
for x in range(1, 100):
    if (x % 2) == 0:
        count += 1

print(count)
