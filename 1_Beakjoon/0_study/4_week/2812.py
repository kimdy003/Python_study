"""
2021.10.21
2812_크게 만들기
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().strip()))

stack = []
temp_k = K
for i in range(N):
    while temp_k > 0 and stack:
        if stack[-1] < num[i]:
            temp_k -= 1
            stack.pop()
        else:
            break
    stack.append(num[i])

end = N - K
print("".join(list(map(str, stack))[:end]))
