# 遍历字符串
name = "qianrui"

# for循环处理字符串
# 将字符串中的每个字符取出进行遍历
for x in name:
    print(x, end='')

print()
count = 0
name = "ItHeima is a brand of ItCast"

for x in name:
    if x == "a":
        count += 1
print(name, end='')
print("这个字符串里面有%d个\"a\"" % count)
