#추석 트래픽
def solution(lines):
    ans = 0
    ret = []
    for line in lines:
        t_list = line.split(" ")

        hour, min, sec = t_list[1].split(":")
        hour = int(hour)*1000*3600
        min = int(min)*1000*60
        sec = int(sec[0:2] + sec[3:])
        s = hour + min + sec

        lst = t_list[2][:-1].split('.')
        duration = int(lst[0])*1000
        if len(lst) > 1:
            duration += int(lst[1] + ('0'*(3-len(lst[1]))))

        ret.append([s-duration+1, s])

    for i in range(len(ret)):
        temp = 0
        begin = ret[i][1]
        end = begin + 999

        for j in range(i, len(ret)):
            if not (ret[j][1] < begin or end < ret[j][0]):
                temp += 1

        ans = max(ans, temp)
    return ans


solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])