def solution(routes):
    answer, camera = 0, 0
    visit = []
    routes.sort(key= lambda x : x[1])
    
    for idx, route in enumerate(routes):
        if idx in visit:
            continue;
        answer += 1
        camera = route[1]
        for idx, r in enumerate(routes):
            if r[0] <= camera <= r[1]:
                visit.append(idx)
    
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))