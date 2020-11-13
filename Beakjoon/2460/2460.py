passenger = 0
Max_passenger = 0

for _ in range(10):
    Out, In = map(int, input().split())
    passenger += In - Out
    Max_passenger = max(passenger, Max_passenger)

print(Max_passenger)