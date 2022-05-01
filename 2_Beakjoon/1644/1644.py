#
#  1644.py
#  소수의 연속합
#
#  Create by 김도영 on 2021/05/14
#


from sys import stdin

input = stdin.readline
N = int(input())
answer = 0

lst = []
board = [False, False] + [True] * (N - 1)

# 에라토스테네스의 체
for i in range(2, N + 1):
    if board[i] == True:
        lst.append(i)
        for j in range(i * i, N + 1, i):
            board[j] = False

Sum = 0
start, end = 0, 0
while True:
    if Sum >= N:
        if Sum == N:
            answer += 1
        Sum -= lst[start]
        start += 1
    elif end == len(lst):
        break
    else:
        Sum += lst[end]
        end += 1

print(answer)