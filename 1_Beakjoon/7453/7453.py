#
#  7453.py
#  합이 0인 네 정수
#
#  Create by 김도영 on 2021/04/23
#


import sys


N = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab, cd = [], []
for i in range(N):
    for j in range(N):
        ab.append(A[i] + B[j])
        cd.append(C[i] + D[j])

ab.sort()
cd.sort()
res, l, r = 0, 0, len(cd) - 1
while l < len(ab) and r >= 0:
    if ab[l] + cd[r] > 0:
        r -= 1
    elif ab[l] + cd[r] < 0:
        l += 1
    else:
        a, b = 1, 1
        while l < len(ab) - 1 and ab[l + 1] == ab[l]:
            l, a = l + 1, a + 1
        while r > 0 and cd[r - 1] == cd[r]:
            r, b = r - 1, b + 1
        res += a * b
        l, r = l + 1, r - 1

print(res)