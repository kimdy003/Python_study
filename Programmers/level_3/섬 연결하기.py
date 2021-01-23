def solution(n, costs):
    costs.sort()
    connect = set([costs[0][0]])
    answer = 0

    while len(connect) != n:
        for i, cost in enumerate(costs):
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))