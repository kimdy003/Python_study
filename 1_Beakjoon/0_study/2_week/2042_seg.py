"""
2021.10.22
2042_구간 합 구하기 (세그먼트 트리)
"""

import sys

input = sys.stdin.readline

# 세그먼트 트리 생성
def Init(node, start, end):
    # node가 leaf 노드인 경우 배열의 원소 값을 반환
    if start == end:
        tree[node] = lst[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장
        tree[node] = Init(node * 2, start, mid) + Init(
            node * 2 + 1, mid + 1, end
        )
        return tree[node]


def Update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff
    # 리프 노드가 아닌 경우
    # 자식도 변경해줘야 하기 때문에 검사해야함
    if start != end:
        mid = (start + end) // 2
        Update(node * 2, start, mid, index, diff)
        Update(node * 2 + 1, mid + 1, end, index, diff)


# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 담당하는 구간 [left, right]
def Subsum(node, start, end, left, right):
    # 겹치지 않기 때문에, 더 이상 탐색을 이어갈 필요가 없다.
    if left > end or right < start:
        return 0

    # 구해야 하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함되고
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율
    if left <= start and end <= right:
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야 한다.
    mid = (start + end) // 2
    return Subsum(node * 2, start, mid, left, right) + Subsum(
        node * 2 + 1, mid + 1, end, left, right
    )


N, M, K = map(int, input().split())
lst = []
tree = [0] * 3000000

for _ in range(N):
    lst.append(int(input()))

Init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:  # b번째 수를 c로 변경
        b = b - 1
        diff = c - lst[b]
        lst[b] = c
        Update(1, 0, N - 1, b, diff)
    elif a == 2:  # b부터 c까지 출력
        print(Subsum(1, 0, N - 1, b - 1, c - 1))
