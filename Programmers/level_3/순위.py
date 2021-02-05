def solution(n, results):

    #wins[i] : i번 선수에게 진 선수들
    #loses[i] : i번 선수에게 이긴 선수들
    wins, loses = {}, {}
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for res in results:
            if res[0] == i:
                wins[i].add(res[1])
            if res[1] == i:
                loses[i].add(res[0])
        
        #loses[i]로 인해 i를 이긴 선수들은 i에게 진 선수들은 무조건 이긴다.
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])
    
    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            cnt += 1

    return cnt

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))