def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def solution(arr):
    def lcm(x, y):
        return x*y // gcd(x, y)
    
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]