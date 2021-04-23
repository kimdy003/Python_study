#
#  1339.py
#  단어 수학
#
#  Create by 김도영 on 2021/04/22
#

from sys import stdin

n = int(stdin.readline())
words = [stdin.readline().strip() for _ in range(n)]

dict = {}
for word in words:
    k = len(word) - 1
    for s in word:
        dict[s] = dict.get(s, 0) + pow(10, k)
        k -= 1

nums = []

for val in dict.values():
    nums.append(val)
nums.sort(reverse=True)

result, t = 0, 9

for i in range(len(nums)):
    result += nums[i] * t
    t -= 1

print(result)