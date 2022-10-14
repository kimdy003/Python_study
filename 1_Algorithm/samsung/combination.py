def comb(arr, r):
    ans = []
    arr = sorted(arr)

    def generate(result):
        if len(result) == r:
            ans.append(result[:])
            return

        start = arr.index(result[-1]) + 1 if result else 0
        for nxt in range(start, len(arr)):
            result.append(arr[nxt])

            generate(result)

            result.pop()

    generate([])
    return ans


arr = [1, 2, 3]
print(comb(arr, 1))  # [[1], [2], [3]]
print(comb(arr, 2))  # [[1, 2], [1, 3], [2, 3]]
print(comb(arr, 3))  # [[1, 2, 3]]
