import sys

input = sys.stdin.readline

if __name__ == "__main__":
    target, N = int(input()), int(input())
    remote = {str(x) for x in range(10)} - set(input().split())

    minCount = abs(100 - target)

    for nums in range(1000001):
        for num in str(nums):
            if num not in remote:
                break
        else:
            minCount = min(minCount, len(str(nums)) + abs(nums - target))
    print(minCount)
