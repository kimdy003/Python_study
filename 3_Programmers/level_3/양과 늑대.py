def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep + (info[child] ^ 1), wolf + info[child])
                visited[child] = 0

    dfs(1, 0)
    return max(answer)


print(
    solution(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
    )
)
