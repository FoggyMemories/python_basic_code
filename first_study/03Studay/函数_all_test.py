def menu():
    print(f"{name}你好")
    print("欢迎来到银行操作系统")
    print("1 : 查询余额")
    print("2 : 进行存款")
    print("3 : 进行取款")
    print("4 : 显示主菜单")
    print("5 : 退出程序")


def query():
    print("----------余额查询-----------")
    print(f"{name},你好,您账户的余额剩余:{money}元")


def deposit():
    print("请输入您要存入钱的数目:")
    i = int(input())
    global money
    money += i
    print(f"{name},你好,您账户的余额剩余:{money}元")


def withdrawal():
    print("请输入您要取出钱的数目:")
    i = int(input())
    global money
    money -= i
    if money >= 0:
        print(f"{name},你好,您账户的余额剩余为:{money}元")
    else:
        print(f"{name},你好,您账户的余额剩余为:0元")


money = 5000000
name = input("请输入用户的名字:")

menu()

while True:
    print("请输入您的选择")
    num = int(input())
    match num:
        case 1:
            query()
        case 2:
            deposit()
        case 3:
            withdrawal()
        case 4:
            menu()
        case 5:
            break
