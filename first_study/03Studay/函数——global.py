num = 200


def test_a():
    print(num)


def test_b():
    global num  # 设置内部定义的变量为全局变量
    num = 500
    print(num)


print(num)  # 当没有运行test_b的时候，全局变量没有发生改变
test_a()
print(num)  # 运行test_a的时候,test_a中并没有改变全局变量的的表达式,所以说也没有发生改变
test_b()
print(num)
