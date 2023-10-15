def check(num):
    if num > 37.5:
        return False
    else:
        return True


num = int(input("请输入你当前的体温"))
if check(num):
    print("您当前的提问是%s,没有问题" % num)
else:
    print("您当前的提问是%s,需要隔离" % num)
