from sys import stdin

n, k = map(int, stdin.readline().split())
queue = [i+1 for i in range(n+1)]
answer = []

idx = 0
while len(queue) > 0:
    idx = (idx+(k-1)) % len(queue)
    element = queue.pop(idx)
    answer.append(str(element))

print("<%s>" %(", ".join(answer)))