#
#  lv2_가장 큰 수.py
#  lv2_가장 큰 수 
#
#  Create by 김도영 on 2021/04/21
#


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))