from math import ceil, log2


def init(tree):
    for idx in range(N - 1, 0, -1):
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


def query(tree, left, right):
    result = 0
    left, right = left + N, right + N

    while left < right:
        # left가 가리키는 노드가 오른쪽 자식이면 현재 누적합을 더해주고 + 1
        if left % 2 == 1:
            result += tree[left]
            left += 1
        # right가 가리키는 노드가 왼쪽 자식이면 현재 누적합을 더해주고 - 1
        if right % 2 == 0:
            result += tree[right]
            right -= 1

        left, right = left // 2, right // 2

    # 서로 같은 구간을 가리키면 마지막으로 현재 구간의 누적합을 더해줌
    if left == right:
        result += tree[left]
    return result


def update(tree, idx, val):
    tree[N + idx] = val
    idx += N

    while idx > 1:
        parent = idx // 2
        tree[parent] = tree[idx]
        if idx % 2 == 0:  # 왼쪽 자식일 경우
            tree[parent] += tree[idx + 1]
        else:  # 오른쪽 자식일 경우
            tree[parent] += tree[idx - 1]
        idx = parent


if __name__ == "__main__":
    N = 6
    arr = [1, 3, 5, 2, 6, 4]
    segmentTree = [0] * pow(2, ceil(log2(N) + 1))
    for i in range(N):
        segmentTree[N + i] = arr[i]
    init(segmentTree)
    print(f"segment tree : {segmentTree}")

    print(f"idx 1 to 3 : {arr[1:4]}")
    print(f"sum 1 to 3 : {query(segmentTree, 1, 3)}")

    update(segmentTree, 1, 4)  # arr[1]의 값을 4로 바꾸기
    arr[1] = 4
    print(f"idx 1 to 3 : {arr[1:4]}")
    print(f"sum 1 to 3 : {query(segmentTree, 1, 3)}")

    N = 8
    segmentTree = [0] * (2 * N)
    update(segmentTree, 0, 1)
    update(segmentTree, 1, 3)
    update(segmentTree, 2, 5)
    update(segmentTree, 3, 6)
    update(segmentTree, 4, 8)
    update(segmentTree, 5, 2)
    update(segmentTree, 6, 6)
    update(segmentTree, 7, 11)
    print(query(segmentTree, 3, 6))
    update(segmentTree, 4, 3)
    print(query(segmentTree, 3, 6))
    print(segmentTree)
