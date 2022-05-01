import sys

sys.setrecursionlimit(10 * 7)


def solution(lst):
    answer = []

    def backtrak(s, sset, l):
        if len(s) > length:
            return
        sset.add(s)

        temp = s
        # x개만큼 'b' 추가
        s = ("b" * l) + s + ("b" * l)
        backtrak(s, sset, l)
        s = temp

        # 맨 앞 'a' 추가
        s = "a" + s
        backtrak(s, sset, l + 1)
        s = temp

        # 맨 뒤 'a' 추가
        s = s + "a"
        backtrak(s, sset, l + 1)
        s = temp

        return

    sset = set()
    length = 22
    backtrak("a", sset, 1)

    for a in lst:
        if a in sset:
            answer.append(True)
        else:
            answer.append(False)

    return answer


print(solution(["abab", "bbaa", "bababa", "bbbabababbbaa"]))
