Min = 987654321

def DFS(n, battery, Sum):
    gloab
    if Sum >= Min:
        return

    if n <= 0:
        global Min
        if Min > Sum:
            Min = Sum
        return
    
    
    for i in battery:
        DFS(n-i[0], battery, Sum+i[1])
    
    return

def solution(n, battery):
    for i in battery:
        temp = n // i[0]
        cnt = temp * i[0]
        price = temp * i[1]
        DFS(n - cnt, battery, price)
    return Min

l = [[6,30000],[3,18000],[4,28000],[1,9500]]
solution(20, l)