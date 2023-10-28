"""
演示函数综合案例开发
"""

# 定义全局变量
money = 500000
name = None

# 要求用户输入姓名
name = input("请输入您的姓名:")


# 定义查询函数
def query(show_header):
    if show_header:
        print("--------------余额查询--------------")
    print(f"{name},您好,您的余额剩余:{money}元")


# 定义存款函数
def saving(num):
    global money
    money += num
    print("--------------存款--------------")
    print(f"{name},您好,您存款{num}元成功.")

    # 调用query函数查询余额
    query(False)


# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("--------------取款--------------")
    print(f"{name},您好,您取款{num}元成功.")

    # 调用query函数查询余额
    query(False)


# 定义主菜单函数
def main():
    print("--------------主菜单--------------")
    print(f"{name},您好,欢迎来到ATM机,请选择您的操作:")
    print("查询余额\t[输入1]")
    print("存款\t[输入2]")
    print("取款\t[输入3]")
    print("退出\t[输入4]")
    return input("请输入您的选择:")


# 设置无限循环,确保程序不会退出
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("请输入存入的金额:"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入取出的金额:"))
        get_money(num)
        continue
    else:
        print("程序退出")
        break  # 退出循环
