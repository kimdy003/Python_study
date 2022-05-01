ans = 0

def Backtrak(paper, n):
    global ans
    ans = max(ans, max(paper))
    if n == 0:
        return
        
    for i in range(1, len(paper)):
        left = paper[:i]
        right = paper[i:]

        if len(left) < len(right):
            idx = 0
            for l in reversed(left):
                right[idx] += l
                idx += 1
            Backtrak(right, n-1)
        
        else:
            idx = len(left)-1
            for r in right:
                left[idx] += r
                idx -= 1
            Backtrak(left, n-1)
    return


def solution(paper, n):
    global ans

    Backtrak(paper, n)
    return ans

print(solution([7, 3, -7, 5, -3], 2))