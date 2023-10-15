"""
演示字符串的三种定义方式:
- 单引号定义法
- 双引号定义法
- 三引号定义法
"""

# 单引号定义发,使用单引号进行包围
name = '钱睿'
print(type(name))

# 双引号定义法
name = "钱睿"
print(type(name))

# 三引号定义法
name = """钱睿"""
print(type(name))

# 在字符串内 包含双引号
name = '钱"\n"睿'
print(name)

# 在字符串内 包含单引号
name = "钱'\n'睿"
print(name)

# 使用转移字符 \ 解除引号的效用
name = "钱\"睿"
print(name)
