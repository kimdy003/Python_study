array = []

for i in range(1, 46):
    array += [i] * i

a, b = map(int, input().split())
print(sum(array[a-1:b]))