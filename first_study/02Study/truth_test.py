import random

random_number = random.randint(1, 100)

print("现在已经产生了一个1 ~ 100的随机数字,请你来猜出来这个数")
count = 0
while True:
    user_input = int(input("请输入所猜测的数字:"))
    count += 1
    if user_input > random_number:
        print("您所猜的数字大了")
    elif user_input == random_number:
        print("恭喜你,猜对了")
        break
    else:
        print("您所猜的数字小了")

print("这个数字是:%d" % random_number)
print("您所猜的次数为:%d" % count)
