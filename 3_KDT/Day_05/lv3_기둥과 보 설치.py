#
#  lv3_기둥과 보 설치.py
#  기둥과 보 설치
#
#  Create by 김도영 on 2021/04/29
#


def Impossible(ret):
    pill, bo = 0, 1
    for x, y, a in ret:
        if a == pill:  # 기둥
            if (
                (y != 0)
                and ((x, y - 1, pill) not in ret)
                and ((x - 1, y, bo) not in ret)
                and ((x, y, bo) not in ret)
            ):
                return True
        else:
            if (
                ((x, y - 1, pill) not in ret)
                and ((x + 1, y - 1, pill) not in ret)
                and (not ((x - 1, y, bo) in ret and (x + 1, y, bo) in ret))
            ):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b:
            result.add(item)
            if Impossible(result):
                result.remove(item)

        elif item in result:
            result.remove(item)
            if Impossible(result):
                result.add(item)

    return sorted(list(result), key=lambda x: (x[0], x[1], x[2]))
