import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    S = int(input())

    for i in range(N):
        # 탐색
        maxNum = max(lst[i : min(N, i + S + 1)])
        idx = lst.index(maxNum)
        
        for j in range(idx, i, -1):
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
        
        S -= (idx - i)
        if S <= 0: break
    
    print(*lst)