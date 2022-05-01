from collections import deque

def solution(jobs):
    answer = 0
    ret = []

    time = 0

    while True:
        if len(ret) == len(jobs):
            break

        temp = []
        for idx, job in enumerate(jobs):
            if idx in ret:
                continue
            if job[0] <= time:
                temp.append( (idx, job[0], job[1]) )

        if len(temp) == 0:
            time += 1
            continue

        temp.sort(key= lambda x : x[2])
        time += temp[0][2]
        answer += (time - temp[0][1])
        ret.append(temp[0][0])
        

    return answer//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))