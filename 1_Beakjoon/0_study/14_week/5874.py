import sys

input = sys.stdin.readline

string = input().strip()
ans, temp = 0, 0

for i in range(len(string)):
    if string[i : i + 2] == "((":
        temp += 1
    elif string[i : i + 2] == "))":
        ans += temp

print(ans)
