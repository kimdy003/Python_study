def solution(code, day, data):
    answer = []
    
    for d in data:
        lst = d.split()
        lst_price = lst[0][6:]
        lst_code = lst[1][5:]
        lst_time = lst[2][5: 13]
        priority = int(lst[2][13:])
        
        if lst_code == code and lst_time == day:
            answer.append((priority, int(lst_price)))
    
    answer = sorted(answer, key=lambda x : x[0])
    ans = [i[1] for i in answer]
    return ans