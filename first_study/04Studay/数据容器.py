test_list = ["123", 123, True, 'A', 12.31]
print(test_list)
print(len(test_list))
print(type(test_list))
for i in range(len(test_list)):
    print(test_list[i], end='')

print()
test_list_2 = [[1, 2, 3], [3, 4, 5]]
print(test_list_2)
print(len(test_list_2))
print(type(test_list_2))
for i in range(len(test_list_2)):  # 此时list的长度为2
    print(test_list_2, end='')

print()
print(test_list[-2])  # 将列表的索引从后往前，依次是-1， -2， -3， .....
print(test_list_2[0][-2])

print()
for i in range(-1, -(len(test_list) + 1), -1):
    print(test_list[i], end='')

print()
for i in range(len(test_list_2)):
    for j in range(len(test_list_2[i])):
        print(test_list_2[i][j], end='')
    print()

test_list_3 = {2}
for i in range(len(test_list_3)):
    test_list_3[i] = input(f"请输入第{i}位索引的元素个")
