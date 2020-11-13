result = []

for i in range(5):
    num = list(map(int, input().split()))
    result.append(sum(num))

Max = max(result)
Max_idx = 0

for i in range(len(result)):
    if Max == result[i]:
        Max_idx = i

print(Max_idx+1, Max)
