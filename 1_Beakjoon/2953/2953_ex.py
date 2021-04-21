Max = 0
idx = 0
for i in range(5):
    num = sum(list(map(int, input().split())))
    if Max < num:
        Max = num
        idx = i
   

print(idx, Max)