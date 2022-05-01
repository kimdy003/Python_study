def solution(n, k, cmd):
    lst = [i for i in range(n)]
``
    idx = k
    temp = []
    for c in cmd:

        if len(c) == 1:
            if c == "C":
                temp.append((idx, lst))
                lst = lst[:idx] + lst[idx + 1 :]
                if idx == len(lst):
                    idx -= 1

            else:
                t = temp.pop()
                pos = t[0]
                lst = t[1]

                if pos <= idx:
                    idx += 1

        else:
            c = c.split()
            if c[0] == "U":
                idx -= int(c[1])
            else:
                idx += int(c[1])

            idx = idx % len(lst)

    answer = ""
    r_idx = 0
    for n in range(n):
        if n == lst[r_idx]:
            answer += "O"
            r_idx += 1
        else:
            answer += "X"

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
