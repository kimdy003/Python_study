g_lion = []
score = 0


def check(info, lion):
    global g_lion, score
    p_score, l_score = 0, 0
    for i, (p, l) in enumerate(zip(info, lion)):
        if p != 0 and p >= l:
            p_score += 10 - i
        elif l != 0 and p < l:
            l_score += 10 - i

    if score < l_score - p_score:
        score = l_score - p_score
        g_lion = lion[:]
    elif score == l_score - p_score:
        # 가장 낮은 점수를 많이 맞힌
        for (g, l) in zip(g_lion[::-1], lion[::-1]):
            if g < l:
                g_lion = lion[:]
                break
            elif g > l:
                break
    return


def backtrak(idx, n, lion, info):
    if idx == 11:
        check(info, lion)
        return

    for i in range(0, n + 1):
        lion[idx] = i
        backtrak(idx + 1, n - i, lion, info)
        lion[idx] = 0


def solution(n, info):
    lion = [0 for _ in range(11)]

    backtrak(0, n, lion, info)
    print(g_lion)
    return g_lion if g_lion else [-1]


print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
