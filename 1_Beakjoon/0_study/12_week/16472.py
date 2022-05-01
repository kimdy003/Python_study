import sys

input = sys.stdin.readline

N = int(input())
string = input().strip()

dic = {}
ans = [0, 0]
left, right = 0, 0

while left < len(string) and right < len(string):
    if string[right] not in dic:
        dic[string[right]] = 1
    else:
        dic[string[right]] += 1

    while len(dic) > N and left <= right:
        if dic[string[left]] == 1:
            dic.pop(string[left])
        else:
            dic[string[left]] -= 1
        left += 1

    if ans[1] - ans[0] < right - left:
        ans = [left, right]

    right += 1

print(ans[1] - ans[0] + 1)
