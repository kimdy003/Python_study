# 21.07.04
# 오름차순 정렬 거리가 k이하만큼 이동 가능
ans = 1e9


def DFS(arr, K, dict, cnt, ans_list, key, flag):
    if arr == ans_list:
        global ans
        ans = min(ans, cnt)
        return

    my_point, current = key - 1, dict[key]
    if my_point == current:
        if flag:
            DFS(arr, K, dict, cnt, ans_list, key + 1, flag)
        else:
            DFS(arr, K, dict, cnt, ans_list, key - 1, flag)

    idx = K
    if my_point < current:
        for kk in range(K, 0, -1):
            next = current - kk
            if my_point > next:
                idx -= 1
            elif arr[next] == current + 1:
                dict[arr[next]] = current
                dict[key] = next
                arr[current], arr[next] = arr[next], arr[current]

                DFS(arr, K, dict, cnt + 1, ans_list, key, flag)

                dict[arr[next]] = next
                dict[key] = current
                arr[current], arr[next] = arr[next], arr[current]
                break
        else:
            next = current - idx
            dict[arr[next]] = current
            dict[key] = next
            arr[current], arr[next] = arr[next], arr[current]

            DFS(arr, K, dict, cnt + 1, ans_list, key, flag)

            dict[arr[next]] = next
            dict[key] = current
            arr[current], arr[next] = arr[next], arr[current]

    elif my_point > current:
        # 자기 자리보다 왼쪽에 있으므로 오른쪽으로 가야된다
        for kk in range(K, 0, -1):
            next = current + kk
            if my_point < next:
                idx -= 1
            elif arr[next] == current + 1:  # 이동 가능
                dict[arr[next]] = current
                dict[key] = next
                arr[current], arr[next] = arr[next], arr[current]

                DFS(arr, K, dict, cnt + 1, ans_list, key, flag)

                dict[arr[next]] = next
                dict[key] = current
                arr[current], arr[next] = arr[next], arr[current]
                break
        else:
            next = current + idx
            dict[arr[next]] = current
            dict[key] = next
            arr[current], arr[next] = arr[next], arr[current]

            DFS(arr, K, dict, cnt + 1, ans_list, key, flag)

            dict[arr[next]] = next
            dict[key] = current
            arr[current], arr[next] = arr[next], arr[current]


def solution(arr, k):
    ans_list = sorted(arr)
    dict = {}
    for i in range(len(arr)):
        dict[arr[i]] = i

    DFS(arr, k, dict, 0, ans_list, 1, True)
    DFS(arr, k, dict, 0, ans_list, len(arr), False)

    return ans


print(solution([4, 5, 2, 3, 1], 2))
