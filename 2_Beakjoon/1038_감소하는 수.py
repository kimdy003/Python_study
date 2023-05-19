import sys

input = sys.stdin.readline


def com(arr, r):
    ans = []

    def generate(result, start):
        if len(result) == r:
            ans.append(result[:])
            return

        for i in range(start, len(arr)):
            result.append(arr[i])
            generate(result, i + 1)
            result.pop()

    generate([], 0)
    return ans


if __name__ == "__main__":
    ans = []
    N = int(input())

    for i in range(1, 11):
        for comb in com(range(0, 10), i):
            comb.sort(reverse=True)
            ans.append(int("".join(map(str, comb))))

    ans.sort()
    print(ans)

    print(ans[N] if len(ans) > N else -1)
