from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    cand = []
    for i in range(1, col+1):
        cand.extend(combinations(range(col), i))
    
    unique = []
    for c in cand:
        temp = [tuple([item[i] for i in c]) for item in relation]
        if len(set(temp)) == row:
            unique.append(c) 

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):    # & : 합집합
                # remove()와 비슷 , discard()는 지우려는 element가 없어도 정상적으로 종료
                answer.discard(unique[j])  
    
    return len(answer)


print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))