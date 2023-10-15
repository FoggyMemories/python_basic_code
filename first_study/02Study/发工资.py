"""
某公司,账户余额有1w元,给20名员工发工资
    员工编号从1 ~ 20,从编号1开始,依次领取工资,没人课领取1000元
    领取工资时,财务判断员工的绩效分(1 ~ 10)(随机生成) ,如果低于5,不发工资,换下一位
    如果工资发完了,结束发工资
"""

import random

all_money = 10000

for i in range(1, 21):
    score = random.randint(1, 11)
    print("第%d个员工的绩效分数为%d" % (i, score))
    if score >= 5:
        all_money -= 1000
        if all_money >= 0:
            print("剩余的奖金为%d" % all_money)
        else:
            break
    else:
        print("该员工的绩效分数过低,没有奖金")