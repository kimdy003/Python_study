a = int(input())
b = int(input())
c = int(input())

num = a * b * c
num_list = list(str(num))

for i in range(10):
    count = num_list.count(str(i))
    print(count)