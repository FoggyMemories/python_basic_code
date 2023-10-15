print("欢迎来到立达动物园")

height = int(input("请输入你的身高"))
if height > 120:
    print("您的身高大于120cm,不能免费")
    print("如果你的vip等级高于3,可以免费游玩")

    vip_num = int(input("请输入你的vip等级"))
    if vip_num > 3:
        print("您的vip等级为%d,可以免费游玩" % vip_num)
    else:
        print("您的vip等级为%d,需要补票10元" % vip_num)

else:
    print("欢迎你大学生,你可以免费进行游玩")