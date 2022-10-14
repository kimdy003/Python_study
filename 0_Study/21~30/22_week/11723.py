import sys

input = sys.stdin.readline


class solve:
    def __init__(self):
        self.S = [0 for _ in range(21)]

    def add(self, x):
        if self.S[x] == 0:
            self.S[x] = 1

    def remove(self, x):
        if self.S[x] == 1:
            self.S[x] = 0

    def check(self, x):
        if self.S[x] == 1:
            print(1)
        else:
            print(0)

    def toggle(self, x):
        if self.S[x] == 0:
            self.S[x] = 1
        else:
            self.S[x] = 0

    def all(self):
        self.S = [1 for _ in range(21)]

    def empty(self):
        self.S = [0 for _ in range(21)]


sol = solve()
N = int(input())
for _ in range(N):
    order = input().split()

    if len(order) == 1:
        if order[0] == "all":
            sol.all()
        else:
            sol.empty()
        continue

    if order[0] == "add":
        x = int(order[1])
        sol.add(x)
    elif order[0] == "remove":
        x = int(order[1])
        sol.remove(x)
    elif order[0] == "check":
        x = int(order[1])
        sol.check(x)
    elif order[0] == "toggle":
        x = int(order[1])
        sol.toggle(x)
