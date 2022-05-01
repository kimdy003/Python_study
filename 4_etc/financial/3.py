def solution(logs):
    answer = []
    dic, i = {}, 0
    for log in logs:
        idx, num, score = log.split()
        if idx not in dic:
            dic[i] = idx
            i += 1

    print(dic)
    return answer


print(
    solution(
        [
            "0001 3 95",
            "0001 5 90",
            "0001 5 100",
            "0002 3 95",
            "0001 7 80",
            "0001 8 80",
            "0001 10 90",
            "0002 10 90",
            "0002 7 80",
            "0002 8 80",
            "0002 5 100",
            "0003 99 90",
        ]
    )
)
