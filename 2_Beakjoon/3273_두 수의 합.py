import sys

input = sys.stdin.readline

if __name__ == "__main__":
    ans = 0
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    x = int(input())

    left, right = 0, N - 1
    while left < right:
        Sum = lst[left] + lst[right]
        if Sum < x:
            left += 1
            continue

        elif Sum == x:
            ans += 1
        right -= 1

    print(ans)
