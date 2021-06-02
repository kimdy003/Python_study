import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))

count = Counter(card)
print(count)

M = int(input())
arr = list(map(int, input().split()))

for a in arr:
    print(count[a], end=" ")
