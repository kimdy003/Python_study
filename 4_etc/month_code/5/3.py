def solution(S):
    answer = []

    for s in S:
        idx = 0
        size = len(s)
        while idx < size - 2:
            if s[idx : idx + 3] == "110":
                s = s[:idx] + s[idx + 3 :]

                temp = [("110" + s, 3), (s + "110", len(s) + 4)]
                for i, k in enumerate(s):
                    if k == "0":
                        temp.append((s[: i + 1] + "110" + s[i + 1 :], i + 4))
                temp = sorted(temp, key=lambda x: (x[0], -x[1]))
                s, idx = temp[0][0], temp[0][1]
            else:
                idx += 1
        answer.append(s)

    return answer


print(solution(["100111100", "0111111010"]))
