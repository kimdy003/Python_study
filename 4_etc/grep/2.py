score = {
    "A+": 1,
    "A0": 2,
    "A-": 3,
    "B+": 4,
    "B0": 5,
    "B-": 6,
    "C+": 7,
    "C0": 8,
    "C-": 9,
    "D+": 10,
    "D0": 11,
    "D-": 12,
    "F": 13,
}


def solution(grades):

    dic_grades = {}
    for grad in grades:
        num, sc = grad.split()

        if num not in dic_grades:
            dic_grades[num] = sc
            continue

        if score[dic_grades[num]] > score[sc]:
            del dic_grades[num]
            dic_grades[num] = sc

    temp = []
    for key, val in dic_grades.items():
        sc = score[val]
        temp.append([sc, key, val])

    temp = sorted(temp, key=lambda x: x[0])

    return [" ".join(t[1:]) for t in temp]


print(
    solution(
        [
            "DM0106 D-",
            "PL6677 B+",
            "DM0106 B+",
            "DM0106 B+",
            "PL6677 C0",
            "GP0000 A0",
        ]
    )
)
