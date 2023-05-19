import sys

input = sys.stdin.readline


def prime_list(N):
    sieve = [False, False] + [True] * (N - 1)
    cnt, result = 1, [i for i in range(N + 1)]

    for i in range(2, N + 1):
        if sieve[i] == True:
            cnt += 1
            result[i] = cnt

            for j in range(i + i, N + 1, i):
                if sieve[j] == True:
                    sieve[j] = False
                    result[j] = cnt

    return cnt, result


if __name__ == "__main__":
    N = int(input())
    cnt, result = prime_list(N)
    print(cnt)
    print(*result[1:])
