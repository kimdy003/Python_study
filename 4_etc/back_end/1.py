import re


def solution(registered_list, new_id):
    S = re.compile("[a-z]")
    if new_id not in registered_list:
        return new_id

    S_split, N_split = "", ""
    for i in range(len(new_id)):
        if S.match(new_id[i]) != None:
            S_split += new_id[i]
        else:
            N_split += new_id[i:]
            break
    if len(N_split) == 0:
        N_split = "1"
    else:
        N_split = str(int(N_split) + 1)
    new_id = "".join(S_split + N_split)

    while True:
        if new_id not in registered_list:
            return new_id
        else:
            N_split = str(int(N_split) + 1)
            new_id = "".join(S_split + N_split)


print(solution(["card", "ace15", "ace16", "banker", "ace17", "ace14"], "ace15"))
