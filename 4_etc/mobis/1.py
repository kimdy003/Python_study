def solution(dice):
    answer = 0
    num = [[0, i] for i in range(10)]

    for dic in dice:
        for d in set(dic):
            num[d][0] += 1

    num.sort(key=lambda x: x[0])
    length = len(dice)
    for n in num:
        if n[0] < length and n[1] != 0:
            ans = str(n[1]) * (n[0] + 1)
            return int(ans)


print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))
