# 全局变量关键字 global 在函数内部声明变量为全局变量
def test_a():
    global num  # 设置内部定义的变量为全局变量
    num = 500
    print(f"test_a:{num}")


test_a()
print(num)
