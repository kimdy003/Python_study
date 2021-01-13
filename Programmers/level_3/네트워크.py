def solution(n, computers):
    answer = 0

    visit = list()
    for i in range(n):
        if i in visit:
            continue
        queue = []
        queue.append(i)
        visit.append(i)
        while queue:
            node = queue.pop(0)

            for next in range(len(computers[node])):
                if computers[node][next] and (next not in visit):
                    queue.append(next)
                    visit.append(next)
        answer+=1                    

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))