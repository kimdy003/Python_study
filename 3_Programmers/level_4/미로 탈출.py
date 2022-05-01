import sys

sys.setrecursionlimit(10 * 6)


def solution(n, start, end, roads, traps):
    answer = int(1e9)

    graph = {i: [[], []] for i in range(1, n + 1)}
    Total = 0
    for s, e, w in roads:
        Total += w * 2
        graph[s][0].append([e, w])
        graph[e][1].append([s, w])

    def Backtrack(cur, weight, flag):
        nonlocal answer
        if cur == end:
            answer = min(answer, weight)
            return

        if weight > Total:
            return

        if flag == 0:  # 원래 방향
            for next in graph[cur][flag]:
                if next[0] in traps:  # 다음 node가 traps에 있는 경우
                    Backtrack(next[0], weight + next[1], 1)
                else:
                    Backtrack(next[0], weight + next[1], 0)

        else:  # 바뀐 방향
            for next in graph[cur][flag]:
                if next[0] in traps:
                    Backtrack(next[0], weight + next[1], 0)
                else:
                    Backtrack(next[0], weight + next[1], 1)
        return

    Backtrack(start, 0, 0)

    return answer


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
