def perm(arr, r):
    ans = []
    arr = sorted(arr)
    visited = [0 for _ in range(len(arr))]

    def generate(result, visited):
        if len(result) == r:
            ans.append(result[:])
            return

        for i in range(len(arr)):
            if not visited[i]:
                result.append(arr[i])
                visited[i] = 1

                generate(result, visited)

                result.pop()
                visited[i] = 0

    generate([], visited)
    return ans


print(perm([1, 2, 3], 2))
