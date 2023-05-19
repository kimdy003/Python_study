from math import ceil, log2


def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(arr, tree, node * 2, start, mid) + init(arr, tree, node * 2 + 1, mid + 1, end)

    return tree[node]


# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 담당하는 구간 [left, right]
def subSum(tree, node, start, end, left, right):
    # 겹치지 않기 때문에, 더 이상 탐색을 이어갈 필요가 없다.
    if left > end or right < start:
        return 0

    # 구해야 하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함되고
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율
    if left <= start and end <= right:
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야 한다.
    mid = (start + end) // 2
    return subSum(tree, node * 2, start, mid, left, right) + subSum(tree, node * 2 + 1, mid + 1, end, left, right)


def update(tree, node, start, end, idx, diff):
    if not (start <= idx and idx <= end):
        return

    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(tree, node * 2, start, mid, idx, diff)
        update(tree, node * 2 + 1, mid + 1, end, idx, diff)


if __name__ == "__main__":
    N = 12
    arr = [3, 5, 6, 7, 2, 9, 4, 5, 2, 8, 1, 5]
    segmentTree = [0] * pow(2, ceil(log2(N) + 1))

    init(arr, segmentTree, 1, 0, N - 1)

    print(f"idx 0 to 3 : {arr[0:4]}")
    print(f"sum 0 to 3 : {subSum(segmentTree, 1, 0, N - 1, 0, 3)}")

    print(segmentTree)
    idx, val = 3, 4  # arr[3]의 값을 4로 바꾸기
    diff = 4 - arr[idx]
    update(segmentTree, 1, 0, N - 1, idx, val)
    arr[3] = 4
    print(segmentTree)
