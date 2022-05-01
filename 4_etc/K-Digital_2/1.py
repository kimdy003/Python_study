from itertools import combinations

def solution(math_scores, english_scores):
    answer = 0
    size = len(math_scores)
    place = [[0, 0] for _ in range(size)]

    math_lst = [[math, idx] for idx, math in enumerate(math_scores)]
    math_lst = sorted(math_lst, key=lambda x : x[0], reverse=True)
    english_lst = [[english, idx] for idx, english in enumerate(english_scores)]
    english_lst = sorted(english_lst, key=lambda x : x[0], reverse=True)
    
    for i in range(size):
        place[math_lst[i][1]][0] = i+1
        place[english_lst[i][1]][1] = i+1

    lst = combinations(range(len(math_scores)), 2)
    
    for ll in lst:
        if ((place[ll[0]][0] < place[ll[1]][0]) and (place[ll[0]][1] < place[ll[1]][1])) or ((place[ll[0]][0] > place[ll[1]][0]) and (place[ll[0]][1] > place[ll[1]][1])):
            answer += 1

    return answer

print(solution([70, 65, 90, 80, 50], [40, 20, 30, 60, 50]))