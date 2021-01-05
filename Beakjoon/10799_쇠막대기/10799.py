from sys import stdin

str = list(stdin.readline().strip())
stack = []
ans = 0

for i in range(len(str)):
    if str[i]=='(':
        stack.append(str[i])

    else:
        if i == 0 or str[i-1] == ')':
            ans += 1
            stack.pop()
        
        elif str[i-1] == '(':
            stack.pop()
            ans += len(stack)

print(ans)
