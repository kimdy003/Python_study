import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
