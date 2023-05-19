def perm(arr, r):
    ans = []
    visited = [0 for _ in range(len(arr))]

    def generate(result, visited):
        if len(result) == r:
            ans.append(result[:])
            return

        for idx in range(len(arr)):
            if not visited[idx]:
                result.append(arr[idx])
                visited[idx] = 1

                generate(result, visited)

                result.pop()
                visited[idx] = 0

    generate([], visited)
    return ans


print(perm([1, 2, 3], 2))
print(perm([1, 2, 3], 3))
