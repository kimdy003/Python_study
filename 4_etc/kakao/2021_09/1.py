def solution(id_list, report, k):
    answer = []
    count = {id: 0 for id in id_list}
    user = {id: [] for id in id_list}

    report = list(set(report))
    for re in report:
        s_1, s_2 = re.split()
        user[s_1].append(s_2)
        count[s_2] += 1

    for id in id_list:
        cnt = 0
        for v in user[id]:
            if count[v] >= k:
                cnt += 1
        answer.append(cnt)

    return answer
