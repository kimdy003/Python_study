def solution(leave, day, holidays):
    answer = -1
    if leave == 30:
        return 30

    dd = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    idx = 0
    for i, d in enumerate(dd):
        if d == day:
            idx = i
    month = {(i + 1): dd[(idx + i) % 7] for i in range(31)}

    for i in range(1, 31):
        t_holiday, t_leave = i, leave
        cnt = 0
        while t_holiday != 31:
            if (
                month[t_holiday] == "SAT"
                or month[t_holiday] == "SUN"
                or t_holiday in holidays
            ):
                cnt += 1
            else:
                if t_leave == 0:
                    break

                t_leave -= 1
                cnt += 1

            t_holiday += 1

        answer = max(answer, cnt)

    return answer


print(solution(3, "SUN", [2, 6, 17, 29]))
