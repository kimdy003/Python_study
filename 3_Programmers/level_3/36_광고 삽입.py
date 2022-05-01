def StrToInt(time):
    h, m, s = time.split(':')
    return int(h)*3600 + int(m)*60 + int(s)


def IntToStr(time):
    h = time // 3600
    h = '0'+str(h) if h < 10 else str(h)
    time %= 3600

    m = time // 60
    m = '0'+str(m) if m < 10 else str(m)
    
    s = time % 60
    s = '0'+str(s) if s < 10 else str(s)
    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    play_time = StrToInt(play_time)
    adv_time = StrToInt(adv_time)
    all_time = [0 for _ in range(play_time+1)]

    for log in logs:
        start, end = log.split('-')
        start = StrToInt(start)
        end = StrToInt(end)
        all_time[start] += 1
        all_time[end] -= 1

    #현재 시청자 수
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i-1] + all_time[i]

    #누적 시청자 수
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i-1] + all_time[i]

    most_view = 0
    max_time = 0
    for i in range(adv_time-1, play_time):
        if adv_time <= i:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1
    
    return IntToStr(max_time)



print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))