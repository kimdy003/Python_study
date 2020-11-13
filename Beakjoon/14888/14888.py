import itertools
from functools import reduce
import sys
import time

def insert(length, num, oper):
    ops = {"0": (lambda x,y: x+y), "1": (lambda x,y: x-y), "2": (lambda x,y: x*y), "3": (lambda x,y: x/y)}
    oper_permutation = []
    result = []
    list(oper_permutation.extend([str(index)]*val)
         for index, val in enumerate(oper) if val >0)
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]
    for i in permutation:
        result.append(reduce(lambda x,y: ops[i.pop()](x,y), num))

    print(str(max(result)) + "\n" + str(min(result)))

n = int(input())
num = list(map(int, input().split()))
attri = list(map(int, input().split()))
insert(n, num, attri)
