def solution(s):
    answer = {}
    
    temp = ''
    for i in s:
        if ord('0') <= ord(i) <= ord('9'):
            temp += i
        else:
            if temp == '':
                continue
            if temp in answer:
                answer[temp] += 1
            else:
                answer[temp] = 1
            temp = ''
            
    answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    
    ans = []
    for i in answer:
        ans.append(int(i[0]))
    
    
    return ans

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")