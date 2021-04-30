ans = 987654321


def plus_piece(Str, cnt, strs, t):
    global ans
    if len(t) < len(Str):
        return
    if len(t) == len(Str):
        for a, b in zip(Str, t):
            if a != b:
                break
        else:
            ans = min(ans, cnt)
        return

    idx = len(Str)

    for s in strs:
        for i in range(len(s)):
            if len(t) == idx + i:
                break
            if t[idx + i] != s[i]:
                break
        else:
            plus_piece(Str + s, cnt + 1, strs, t)


def solution(strs, t):
    plus_piece("", 0, strs, t)

    return -1 if ans == 987654321 else ans


print(solution(["ba", "na", "n", "a"], "banana"))
