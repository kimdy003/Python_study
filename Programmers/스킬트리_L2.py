#스킬트리

def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees:
        list = [s.index(i) for i in skill if i in s]
        list_ = sorted(list)
        if list == list_ and all(i in s for i in skill[:len(list)]):
            answer+=1
        
    return answer