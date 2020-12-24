def solution(n):
    J = 0
    while True:
        if not n:
            break
        
        if n%2 == 0:
            n //= 2
        else:
            n -= 1
            J += 1

    return J

#return bin(n).count('1')

