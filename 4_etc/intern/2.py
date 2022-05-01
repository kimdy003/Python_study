def solution(t, r):
    answer = []
    size = max(t)
    dic = {i: [] for i in range(size + 2)}

    for i in range(len(r)):
        dic[t[i]] = dic.get(t[i], []) + [(r[i], t[i], i)]  # 우선순위, 도착 순서, 손님 아이디

    for i in range(size + 1):
        if len(dic[i]) == 1:
            c = dic[i]
            answer.append(c[0][2])

        elif len(dic[i]) > 1:
            c = dic[i]
            c = sorted(c, key=lambda x: (x[0], x[1], x[2]))
            answer.append(c[0][2])
            dic[i + 1] = dic.get(i + 1, []) + c[1:]

    if len(dic[size + 1]):
        for c in dic[size + 1]:
            answer.append(c[2])

    return answer


print(solution([0, 1, 3, 0], [0, 1, 2, 3]))
