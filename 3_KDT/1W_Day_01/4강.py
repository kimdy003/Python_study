# 
#  4강.py
#  피보나치 순열 구현하기
#
#  Created by 김도영 on 2021/04/20.
#

def solution(x):
    
    def Fibonacci(n):
        if n <= 1:
            return n
        return Fibonacci(n-1) + Fibonacci(n-2)
    
    return Fibonacci(x)