import math


def solution(m, musicinfos):
    ans = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for musicIdx, musicinfo in enumerate(musicinfos):
        startTime, endTime, title, code = musicinfo.split(",")

        startTime = int(startTime[:2]) * 60 + int(startTime[3:])
        endTime = int(endTime[:2]) * 60 + int(endTime[3:])
        duration = endTime - startTime

        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        code *= math.ceil(duration / len(code))
        code = code[:duration]

        if m not in code:
            continue

        if ans == None or ans[0] < duration or (ans[0] == duration and ans[1] > musicIdx):
            ans = (duration, musicIdx, title)

    return ans[-1] if ans else "(None)"


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
