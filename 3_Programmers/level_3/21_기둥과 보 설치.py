def Impossible(res):
    pill, Bo = 0, 1
    for x, y, a in res:
        if a == pill:    #기둥
            if (y != 0) and ((x, y-1, pill) not in res) and ((x-1, y, Bo) not in res) and ((x, y, Bo) not in res):
                return True

        else:    #보
            if ((x, y-1, pill) not in res) and ((x+1, y-1, pill) not in res) and (not ((x-1, y, Bo) in res and (x+1, y, Bo) in res)):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b:    #설치
            result.add(item)
            if Impossible(result):    #True일 경우 설치 못함
                result.remove(item)
        elif item in result:
            result.remove(item)
            if Impossible(result):    #True일 경우 제거 못함
                result.add(item)

    answer = map(list, result)

    #a는 구조물 종류 0은 기둥, 1은 보
    #return 배열은 x좌표 기준 오름차순 정렬, x가 같을 경우 y기준 오름차순
    #x, y모두 같을 경우 기둥이 보보다 앞에
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] ))