#
#  3_가장 큰 수.py
#  가장 큰 수
#
#  Create by 김도영 on 2021/04/22
#

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)

    '''
    
    List comprehension (컴프리헨션)
    numbers = sorted([str(x) for x in numbers], key=lambda x : (x * 4)[:4], reverse=True)

    '''
    return str(int(''.join(numbers)))