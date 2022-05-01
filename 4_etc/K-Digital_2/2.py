month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(purchase):
    answer = [0] * 5

    info = []
    for pur in purchase:
        pur = pur.split('/')
        pur = pur[0:2] + pur[2].split()
        
        mon = 0
        for i in range(int(pur[1])):
            mon += month[i]
        mon += int(pur[2])
        info.append([mon, mon+30,int(pur[-1])])
    
    day = [0] * 366
    while info:
        start, end, price = info.pop(0)
        end = min(366, end)
        for i in range(start, end):
            day[i] += price
    
    for i in range(1, len(day)):
        if 0 <= day[i] < 10000:
            answer[0] += 1
        elif 10000 <= day[i] < 20000:
            answer[1] += 1
        elif 20000 <= day[i] < 50000:
            answer[2] += 1
        elif 50000 <= day[i] < 100000:
            answer[3] += 1
        elif 100000 <= day[i]:
            answer[4] += 1

    return answer

print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000", "2019/12/22 90000"]))