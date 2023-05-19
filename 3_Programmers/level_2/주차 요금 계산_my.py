import math


def solution(fees, records):
    answer = []
    lastTime = 1439

    dic = {}
    for record in records:
        time, number, order = record.split()
        h, m = map(int, time.split(":"))
        inTime = 60 * h + m

        if number not in dic:
            dic[number] = [inTime, 0]  # [입차 시간, 누적 주차 시간]

        else:
            if order == "IN":
                dic[number][0] = inTime
            else:
                acc = inTime - dic[number][0]
                dic[number][1] += acc
                dic[number][0] = 0

    for k, v in dic.items():
        if v[0] != 0 or v[1] == 0:
            acc = lastTime - v[0]
            dic[k][1] += acc
            dic[k][0] = 0

    for k, v in sorted(dic.items()):
        if v[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((v[1] - fees[0]) / fees[2]) * fees[3])

    return answer
