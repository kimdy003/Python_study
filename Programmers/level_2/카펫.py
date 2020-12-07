def solution(brown, yellow):
    for x in range(1, yellow+1):
        if not yellow%x:
            y = yellow//x
            if ((x+2)*(y+2)) - (x*y) == brown:
                return [max(x+2, y+2), min(x+2, y+2)]