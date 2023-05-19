import sys

input = sys.stdin.readline


def comb(arr, r):
    ans = []

    def generate(result, start):
        if len(result) == r:
            consonanats = set(result) - vowels

            if len(consonanats) >= 2 and r - len(consonanats) >= 1:
                ans.append(result[:])
            return

        for idx in range(start, N):
            result.append(arr[idx])

            generate(result, idx + 1)

            result.pop()

    generate([], 0)
    return ans


if __name__ == "__main__":
    L, N = map(int, input().split())
    arr = sorted(list(input().strip().split()))
    vowels = set("aeiou")

    for a in comb(arr, L):
        print("".join(a))
