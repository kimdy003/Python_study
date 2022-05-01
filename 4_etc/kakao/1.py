def solution(S):
    dic = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six': '6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    lst, Str=[], ''
    for s in S:
        if Str in dic:
            lst.append(dic[Str])
            Str = ''
        
        if s.isdigit():
            if len(Str) != 0:
                lst.append(dic[Str])
                Str = ''
            lst.append(s)

            
        else:
            Str += s
    
    if len(Str) != 0:
        lst.append(dic[Str])
        
    return int(''.join(lst))