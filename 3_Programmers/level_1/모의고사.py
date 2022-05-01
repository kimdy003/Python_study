#모의고사 

patten = [[1,2,3,4,5],
          [2,1,2,3,2,4,2,5],
          [3,3,1,1,2,2,4,4,5,5]]
    
def solution(answers):
    answer = []
    ret = [0,0,0]
    
    for q, a in enumerate(answers):
        for i, v in enumerate(patten):
            if a == v[q%len(v)]:
                ret[i] += 1
    
    return [i+1 for i, v in enumerate(ret) if v == max(ret)]