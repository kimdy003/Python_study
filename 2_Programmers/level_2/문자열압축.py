#문자열압축

def solution(s):
    answer = 987654321
    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s)//2+1):
        ret = ""
        count = 1
        
        prev = s[:cut]
        
        for i in range(cut, len(s)+cut, cut):
            if s[i:i+cut] == prev:
                count += 1
            else:
                if count == 1:
                    ret = ret + prev
                else:
                    ret = ret + str(count)+prev
                prev = s[i:i+cut]
                count = 1
                
        answer = min(answer, len(ret))
    return min(answer, len(s))