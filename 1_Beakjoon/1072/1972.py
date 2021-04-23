#
#  1972.py
#  게임
#
#  Create by 김도영 on 2021/04/23
#


from sys import stdin


x, y = map(int, stdin.readline().split())
z = int(y * 100 / x)

start, end = 0, 1000000000
while start < end:
    mid = (start + end) // 2
    new_z = int((y + mid) * 100 / (x + mid))
    if new_z <= z:
        start = mid + 1
    else:
        end = mid

print(end if int((y + end) * 100 / (x + end)) > z else -1)