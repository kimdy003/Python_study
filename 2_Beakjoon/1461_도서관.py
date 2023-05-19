import sys

input = sys.stdin.readline


def sol(array):
    result = 0
    if len(array) % 2 == 0:  # 짝수
        for p in array[1:][::M]:
            result += p * 2
    else:
        result += array[0] * 2
        for p in array[2:][::M]:
            result += p * 2

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())

    minus, plus = [], []
    for s in list(map(int, input().split())):
        if s < 0:
            minus.append(-s)
        else:
            plus.append(s)

    minus.sort()
    plus.sort()

    if plus and not minus:
        print(sol(plus) - plus[-1])

    elif not plus and minus:
        print(sol(minus) - minus[-1])

    elif plus and minus:
        # print(minus, plus)

        ans = sol(plus) + sol(minus)
        if minus[-1] > plus[-1]:  # plus 먼저 처리
            ans -= minus[-1]
        else:
            ans -= plus[-1]

        print(ans)
