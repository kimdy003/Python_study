a, b = map(int, input().split())

result_a = 0
result_b = 0

for _ in range(3):
    result_a = (result_a*10) + a%10
    a //= 10

    result_b = (result_b*10) + b % 10
    b //= 10

print(max(result_a, result_b))