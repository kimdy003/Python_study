#
#  12015.py
#  가장 긴 증가하는 부분 수열 2
#
#  Create by 김도영 on 2021/05/05
#


from sys import stdin
import bisect as bs

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

L = [arr[0]]
for a in arr[1:]:
    if L[-1] < a:
        L.append(a)
    else:
        L[bs.bisect_left(L, a)] = a

print(len(L))