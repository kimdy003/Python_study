#완주하지 못한 선수

def solution(p, c):
    p.sort()
    c.sort()
            
    for part, com in zip(p, c):
        if part != com:
            return part
    
    return p[-1]