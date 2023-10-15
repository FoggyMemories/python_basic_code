# 使用input进行数据的输入
print("告诉我你是谁?")
name = input()
print("收到,你是:%s" % name)

# 可以使用input(提示信息),可以在使用者输入内同之前显示提示信息
name = input("请再次告诉我你是谁")
print("我知道了,你是:%s" % name)


# 无论键盘输入的是什么,都是输入的字符串类型,如需转换,则使用强转即可
num = input("请告诉我的年龄:")
print("你的年龄的类型是:", type(num))
# 进行数据的转换
num = int(num)
print(type(num))

