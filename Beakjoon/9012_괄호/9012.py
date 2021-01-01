from sys import stdin

num = int(stdin.readline())

for _ in range(num):
    str = stdin.readline().split()
    stack = []

    for i in str[0]:
        if i == "(":
            stack.append(i)
        
        else:
            if not stack:
                print("NO")
                break
            
            else:
                stack.pop()
    else:
        if not stack:
            print("YES")
        else:
            print("NO")