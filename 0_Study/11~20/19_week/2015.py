import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

dict = {}
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

cnt = 0
for i in range(len(nums)):
    if nums[i] == K:
        cnt += 1
    cnt += dict.get(nums[i] - K, 0)
    dict[nums[i]] = dict.get(nums[i], 0) + 1
print(cnt)
