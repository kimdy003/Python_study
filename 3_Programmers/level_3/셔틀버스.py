def intToStr(time):
    h, m = time // 60, time % 60
    h = "0" + str(h) if h < 10 else str(h)
    m = "0" + str(m) if m < 10 else str(m)
    return h + ":" + m


def solution(n, t, m, timetable):
    timetable = [int(i[:2]) * 60 + int(i[3:]) for i in timetable]
    timetable.sort()
    bustable = [9 * 60 + t * i for i in range(n)]

    for bus in bustable:
        passenger = [p for p in timetable if p <= bus]

        if bus == bustable[-1]:
            if m <= len(passenger):
                answer = passenger[m - 1] - 1
            elif len(passenger) < m:
                answer = bus

        elif len(passenger) < m:
            timetable = timetable[len(passenger) :]

        elif m <= len(passenger):
            timetable = timetable[m:]

    return intToStr(answer)


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
print(
    solution(
        10,
        60,
        45,
        [
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
        ],
    )
)
