from itertools import combinations
import math

def check(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        temp = sum(i)
        if check(temp):    
            answer += 1

    return answer