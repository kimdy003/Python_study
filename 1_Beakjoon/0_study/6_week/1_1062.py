"""
2021.11.13
1062_가르침
"""
import sys
from itertools import combinations

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    pix_alpha = set("antic")
    alpha = [
        a
        for a in set(map(chr, range(ord("a"), ord("z") + 1))).difference(
            pix_alpha
        )
    ]
    words = [set(input().strip()).difference(pix_alpha) for _ in range(N)]

    if K < 5:
        print(0)
    elif K == 26:
        print(N)
    else:
        K -= 5
        ans = 0
        for new in combinations(alpha, K):
            cnt = 0
            for word in words:
                for w in word:
                    if w not in new:
                        break
                else:
                    cnt += 1

            ans = max(ans, cnt)
        print(ans)

    return


solve()
