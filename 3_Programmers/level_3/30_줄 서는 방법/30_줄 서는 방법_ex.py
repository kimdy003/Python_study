def solution(n, k):
    from math import factorial
    answer = []
    order = list(range(1, n+1))
    while n != 0:
        fact = factorial(n-1)
        answer.append(order.pop((k-1)//fact))
        n, k = n-1, k%fact

    return answer

print(solution(3, 5))