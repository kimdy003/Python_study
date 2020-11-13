import sys
import math

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    m = 2000000000
    tmp = 0
    Sum = 0

    for i in range(len(arr)-1):
        Sum += abs(arr[i+1] - arr[i])
    
    while(tmp < arr[n-1]):
        Sum += abs(arr[n-1] - tmp) + abs(arr[0] - tmp)
        if(m > Sum):
            m = Sum
        Sum -= abs(arr[n-1] - tmp) + abs(arr[0] - tmp)
        tmp += 1

    print(m)