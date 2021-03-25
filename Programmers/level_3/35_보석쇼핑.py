def solution(gems):
    size = len(set(gems))
    dic = {gems[0]:1}
    ans = [0, len(gems)-1]
    start, end = 0, 0

    while (start < len(gems)) and (end < len(gems)):
        if len(dic) == size:
            if end - start < ans[1] - ans[0]:
                ans = [start, end]

            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems): break
            dic[gems[end]] = dic.get(gems[end], 0) + 1

    return [ans[0]+1, ans[1]+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))