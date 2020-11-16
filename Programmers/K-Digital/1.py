from functools import reduce

def solution(num):
    answer = 0

    while 1:
        list = []
        temp = num
        while temp != 0:
            list.append(temp%10)
            temp //= 10

        cnt = len(list)
        a = reduce(lambda x, y: x * y, list[:cnt//2])
        b = reduce(lambda x, y: x * y, list[cnt//2:])
        if a == b:
            break
        else:
            num += 1
    
    answer = num
    return answer

n = 21
ans = solution(n)