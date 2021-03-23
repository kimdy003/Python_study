def check(queen, n, row, col):
    for r in range(row):
        q = queen[r]
        
        if col == q:
            return False
        
        a = abs(q - col)
        b = row - r
        if a == b:
            return False
    return True
        

def PlaceQueen(queen, n, row):
    if(row == n):
        return 1
    
    cnt = 0
    for col in range(n):
        if check(queen, n, row, col) == True:
            queen[row] = col
            cnt += PlaceQueen(queen, n, row+1)

    return cnt

def solution(n):
    queen = [0] * n
    answer = PlaceQueen(queen, n, 0)

    return answer

print(solution(4))