def solution(dirs):
    movdir = {"U" : (-1,0), "R":(0, 1), "D":(1, 0), "L":(0, -1)}
    cand = set()
    cur_y, cur_x = (0, 0)

    for dir in dirs:
        ny, nx = cur_y+movdir[dir][0], cur_x+movdir[dir][1]
        if (-5<= ny <= 5) and (-5 <= nx <= 5):
            cand.add((cur_y, cur_x, ny, nx))
            cand.add((ny, nx, cur_y, cur_x))
            cur_y, cur_x = ny, nx
    
    return len(cand)//2

print(solution("ULURRDLLU"))