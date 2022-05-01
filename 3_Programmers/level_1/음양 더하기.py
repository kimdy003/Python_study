def solution(absolutes, signs):
    answer = 0

    for num, oper in zip(absolutes, signs):
        if oper:
            answer += num
        else:
            answer -= num

    return answer