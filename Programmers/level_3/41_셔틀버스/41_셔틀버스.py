def IntToStr(time):
    h, m = time//60, time%60
    h = '0'+str(h) if h < 10 else str(h)
    m = '0'+str(m) if m < 10 else str(m)
    return h + ':' + m


def solution(n, t, m, timetable):
    answer = ''
    lst = []
    for time in timetable:
        lst.append(int(time[:2])*60 + int(time[3:]))
    lst.sort()

    for i in range(n-1):
        start = 9*60 + i*t
        cnt = 0
        while lst and cnt < m:
            if lst[0] <= start:
                del lst[0]
                cnt += 1
            else:
                break
    
    start = 9*60 + (n-1)*t
    cnt = 0
    while lst and cnt < m-1:
        if lst[0] <= start:
            del lst[0]
            cnt+=1
        else:
            break
    
    if not lst or lst[0] > start:
        result = start
    else:
        result = lst[0] -1

    answer = IntToStr(result)

    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))