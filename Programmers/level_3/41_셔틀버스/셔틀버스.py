def IntToStr(time):
    h, m = time//60, time%60
    h = '0'+str(h) if h < 10 else str(h)
    m = '0'+str(m) if m < 10 else str(m)
    return h + ':' + m


def solution(n, t, m, timetable):
    timetable = [int(i[:2])*60+int(i[3:]) for i in timetable]
    timetable.sort()
    bustable = [9*60+t*i for i in range(n)]

    for bus in bustable:
        passenger = [p for p in timetable if p<=bus]

        if bus == bustable[-1]:    #콘이 타야되는 버스
            if m <= len(passenger):
                answer = passenger[m-1]-1
            elif len(passenger) < m:
                answer = bus
        elif len(passenger) < m:
            timetable = timetable[len(passenger):]
        elif m <= len(passenger):
            timetable = timetable[m:]
    
    return IntToStr(answer)

print(solution(2,10,2,["09:10", "09:09", "08:00"]))