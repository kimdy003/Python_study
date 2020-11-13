n = int(float(input()))

for _ in range(n):
    num, Str = input().split()
    num = int(num)
    res = Str[:num-1]
    res2 = Str[num:]
    print(res+res2)