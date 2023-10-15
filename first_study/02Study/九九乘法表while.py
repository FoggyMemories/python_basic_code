"""
默认print语句输出内容会自动换行

如需使用print语句不换行,在print语句后面加上end=''即可

"""

print("这是第一行", end='')
print("这是第二行", end='')
print()
i = 1

while i <= 9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = %d \t" % (i * j), end='')
        j += 1
    print()
    i += 1
