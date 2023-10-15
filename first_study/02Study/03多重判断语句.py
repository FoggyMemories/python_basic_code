print('欢迎来到立达动物园')
height = int(input("请输入您的身高(cm)"))
vip_level = int(input("请输入你的vip等级(1 ~ 5)"))

if height < 120:
    print("您的身高小于120cm,可以免费游玩")
elif vip_level > 3:
    print("您的vip等级大于3级,可以免费游玩")
else:
    print("不好意思,所有条件都不满足,需要购票10元")

print("祝您游玩愉快")
