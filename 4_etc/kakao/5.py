answer = 987654321


def create(prev, node, dic, sum_tree):
    temp = sum_tree[node]
    for nxt in dic[node]:
        if prev == nxt[0]:
            continue

        temp += create(node, nxt[0], dic, sum_tree)

    sum_tree[node] = temp
    return temp


def DFS(prev, node, dic, sum_tree, lst, k):
    global answer
    if len(lst) == k:
        answer = min(answer, max(lst))
        return

    for nxt in dic[node]:
        if nxt == prev:
            continue

    return


def solution(k, num, links):
    if k == 1:
        return sum(num)

    if len(num) == k:
        return max(num)

    dic = {i: [] for i in range(len(num))}

    indegree = [0] * len(num)
    for idx, link in enumerate(links):
        l, r = link
        if l != -1:
            indegree[l] += 1
            dic[idx] += [(l, num[l])]
            dic[l] += [(idx, num[idx])]

        if r != -1:
            indegree[r] += 1
            dic[idx] += [(r, num[r])]
            dic[r] += [(idx, num[idx])]

    root = indegree.index(min(indegree))

    sum_tree = num
    sum_tree[root] = create(-1, root, dic, sum_tree)

    DFS(-1, root, dic, sum_tree, [], k)

    return answer


print(solution(2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
