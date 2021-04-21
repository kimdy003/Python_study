from collections import Counter

def solution(array):
    answer = -1
    element = Counter(array)

    for star in element.keys():
        if element[star] <= answer:
            continue

        cnt = 0
        idx = 0
        while idx < len(array)-1:
            if(array[idx] == array[idx+1]) or(array[idx] != star and array[idx+1] != star):
                idx += 1
                continue

            cnt += 1
            idx += 2
        answer = max(answer, cnt)
    

    return answer*2 if answer != -1 else 0

print(solution([5,2,3,3,5,3]))