a = int(input("请输入层数："))
for i in range(a, 0, -1):
    for y in range(0, a - i, 1):
        print(" ", end='')
    for x in range(0, i * 2 - 1, 1):
        print("*", end='')
    print("\n")


