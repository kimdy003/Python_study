# upgrad : 비용, 걸리는 시간
def solution(time, gold, upgrade):
    time, gold = int(time), int(gold)
    money = [[0, 0] for _ in range(len(upgrade) + 1)]  # 돈 시간

    for t in range(1, time + 1):
        for i in range(1, len(money)):
            if t == 30:
                print(money)

            if money[i][1] == 0 and money[i - 1][0] >= upgrade[i - 1][0]:
                money[i][0] = money[i - 1][0] - upgrade[i - 1][0]
                money[i][1] = 1
                if money[i][1] % upgrade[i - 1][1] == 0:
                    money[i][0] += gold

            elif money[i][1] != 0:
                money[i][1] += 1
                if money[i][1] % upgrade[i - 1][1] == 0:
                    money[i][0] += gold

    money.sort(key=lambda x: -x[0])
    return money[0][0]


print(solution("100", "200", [[0, 5], [1500, 3], [3000, 1]]))
