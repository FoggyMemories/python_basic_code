print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("4 / 2 = ", 4 / 2)
print("9 // 2 = ", 9 // 2)  # 去除后的整数部分
print("9 % 2 = ", 9 % 2)  # 取余
print("2 ** 3 = ", 2 ** 3)  # 指数运算

"""
符合运算符 在普通运算符后面加一个等号 
略
"""

name = "'钱睿'"
print(name)

name = '"钱睿"'
print(name)

name = """
钱睿
22大数据2班
"""
print(name)

num = 123

print("nihao", name, "dajiahao" + name, num)

message = "测试 %s %s" % (123, 321) # 多个变量占位 变量要用括号括起来,并按照占位的顺序填入
print(message)
