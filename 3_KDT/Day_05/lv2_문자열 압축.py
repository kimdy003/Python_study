#
#  lv2_문자열 압축.py
#  문자열 압축
#
#  Create by 김도영 on 2021/04/25
#


def compression(s, i):
    ret = ""
    idx = 0
    while idx < len(s):
        cnt = 1
        while s[idx : idx + i] == s[idx + i : idx + i + i]:
            cnt, idx = cnt + 1, idx + i

        if cnt != 1:
            ret += str(cnt) + s[idx : idx + i]

        else:
            ret += s[idx : idx + i]

        idx += i

    return len(ret)


def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, compression(s, i))

    return answer