name = "钱睿"
massage = "信息: %s" % name
print(massage)

class_num = 57
avg_salary = 16781
message = "Python大数据学科,北京%s期,平均工资:%s" % (class_num, avg_salary)
print(message)

name = "中国政府"
setup_year = 1949
stock_price = 0.01
message = "%s,成立于:%d,我们今天的股价是:%.2f" % (name, setup_year, stock_price)
print(message)
# 快速格式化
# 快速格式化不做精度控制,原样输出,同时不理会类型
print(f"我是{name} 我成立于:{setup_year}, 我们今天的股票价格是: {stock_price:.1f}")
