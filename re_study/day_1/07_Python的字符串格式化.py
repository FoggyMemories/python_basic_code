# 通过占位的形式,完成拼接
name = "钱睿"
message = "是神!%s" % name
print(message)

# 通过占位的形式,完成数字和字符串的拼接
class_num = 57
avg_salary = 156798
message = "大数据毕业,上海%s,平均工资:%s" % (class_num, avg_salary)
print(message)

num1 = 11
num2 = 11.345

print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制17,小数精度2，结果是：%7.2f" % num2)
print("数字11.345不限制宽度,小数精度2，结果是：%.2f" % num2)
