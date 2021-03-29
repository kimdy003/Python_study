def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0]

    memo = [[0 for _ in range(size)] for _ in range(2)]

    memo[0][0] = memo[0][1] = sticker[0]    # 첫번째 스티커를 선택한 경우
    memo[1][1] = sticker[1]    # 첫번째 스티커를 선택하지 않은 경우

    for i in range(2, size-1):
        memo[0][i] = max(memo[0][i-2]+sticker[i], memo[0][i-1])
    
    for i in range(2, size):
        memo[1][i] = max(memo[1][i-2]+sticker[i], memo[1][i-1])

    return max(max(memo[0]), max(memo[1]))

print(solution([1, 3, 2, 5, 4]))