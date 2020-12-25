def solution(n, words):
    answer = [1,0]
    Dict = {}
    
    Dict[words[0]] = 1
    prev = words[0][-1]
    
    for i in range(1, len(words)):
        if words[i] in Dict:
            break
        else:
            Dict[words[i]] = 1
        
        if prev != words[i][0]:
            break
        else:
            prev = words[i][-1]
        
        answer[0] += 1
        if answer[0] == n:
            answer[1] += 1
        answer[0] %= n
    else:
        return [0, 0]
    
    return [answer[0]+1, answer[1]+1]