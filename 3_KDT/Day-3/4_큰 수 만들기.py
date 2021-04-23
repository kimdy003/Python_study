#
#  4_큰 수 만들기.py
#  큰 수 만들기
#
#  Create by 김도영 on 2021/04/22
#


def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    
    return ''.join(collected[:-k] if k > 0 else collected)

print(solution('4177242833', 4))
    