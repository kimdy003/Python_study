def solution(S, C):
    company = "@" + C.lower() + ".com"

    arr = S.split(";")
    lst, cand = [], {}
    for s in arr:
        name = s.split()

        Last_name = name[-1].split("-")
        name.append("".join(Last_name))
        temp = name[-1].lower() + "_" + name[0].lower()

        if temp in cand:
            cand[temp] += 1
            temp += str(cand[temp])
        else:
            cand[temp] = 1

        lst.append("<" + temp + company + ">;")

    answer = ""
    for i in range(len(lst)):
        answer += arr[i] + " " + lst[i]

    return answer[:-1]


print(
    solution(
        "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker",
        "Example",
    )
)
