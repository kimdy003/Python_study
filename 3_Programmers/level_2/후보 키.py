from itertools import combinations


def solution(relation):
    N, M = len(relation), len(relation[0])

    cand = [com for i in range(1, M + 1) for com in combinations(range(M), i)]

    unique = []
    for c in cand:
        temp = [tuple([item[i] for i in c]) for item in relation]
        if len(set(temp)) == N:
            unique.append(c)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)


print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)
