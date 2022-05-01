# 21.07.04
# 복권 구매 평균 구하기


def solution(lottery):
    answer, cnt = 0, 0
    dict = {}
    for lot in lottery:
        dict[lot[0]] = dict.get(lot[0], []) + [lot[1]]

    for key in dict:
        lst = dict[key]
        if max(lst) == 1:
            cnt += 1
            answer += lst.index(max(lst)) + 1

    return answer // cnt if cnt != 0 else 0
