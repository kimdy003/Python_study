from sys import stdin

n = int(stdin.readline().strip())
stack = []
cnt = 0
flag = True

for i in range(1, n+1):
    num = int(stdin.readline().strip())
    
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        print("+")

    if stack[-1] == num:
        stack.pop()
        print("-")
    else:
        flag = False
        break

if not flag:
    print("NO")