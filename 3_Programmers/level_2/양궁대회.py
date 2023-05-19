def calcPoint(apeach, lion):
    apeach_score = 0
    lion_score = 0
    for i in range(11):
        if apeach[i] > lion[i]:
            apeach_score += 10 - i
        elif apeach[i] < lion[i]:
            lion_score += 10 - i

    return lion_score - apeach_score


def dfs(idx, n, apeach, lion):
    global answer, point
    if n < 0:
        return
    if idx == 11:
        diff = calcPoint(apeach, lion)
        if diff > point:
            point = diff
            answer = lion[:]
            answer[10] += n
        return

    lion[10 - idx] = apeach[10 - idx] + 1
    dfs(idx + 1, n - lion[10 - idx], apeach, lion)
    lion[10 - idx] = 0
    dfs(idx + 1, n, apeach, lion)


def solution(n, info):
    global answer, point
    answer = [-1]
    point = 0
    dfs(0, n, info, [0 for _ in range(11)])
    return answer
