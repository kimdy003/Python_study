def solution(records):
    username = []
    dic = {}

    for record in records:
        temp = record.split()
        if temp[0] == "Enter":
            username.append((1, temp[1]))
            dic[temp[1]] = temp[2]
        elif temp[0] == "Leave":
            username.append((2, temp[1]))
        elif temp[0] == "Change":
            dic[temp[1]] = temp[2]

    ans = []
    for user in username:
        if user[0] == 1:
            ans.append("{}님이 들어왔습니다.".format(dic[user[1]]))
        else:
            ans.append("{}님이 나갔습니다".format(dic[user[1]]))

    return ans


print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)
