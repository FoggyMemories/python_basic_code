def fn(a, n):
    count = 1
    sum = 0
    for i in range(1, n + 1):
        sum += a ** count
        count += 1
    return sum


s = fn(2, 3)
print(s)
