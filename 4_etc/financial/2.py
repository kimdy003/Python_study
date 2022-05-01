movdir = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # 하, 좌, 상, 우


def init(n, indexing):
    idx = 1
    temp_field = [[0] * n for _ in range(n)]

    for i in range(n - 1):
        indexing.append([0, i])
        temp_field[0][i] = idx
        idx += 1

    turn, depth = 0, n - 1
    cnt = 0
    y, x = 0, n - 1
    while True:
        if idx > n * n:
            break
        indexing.append([y, x])
        temp_field[y][x] = idx
        y += movdir[turn][0]
        x += movdir[turn][1]
        cnt += 1
        idx += 1

        if cnt == depth:
            if turn in [1, 3]:
                depth -= 1
            turn = (turn + 1) % 4
            cnt = 0


def solution(n, jump):
    answer = []
    indexing = []
    init(n, indexing)

    temp_field = [[0] * n for _ in range(n)]
    idx = 0
    temp_cnt = 1
    temp_field[indexing[idx][0]][indexing[idx][1]] = temp_cnt
    temp_cnt += 1
    del indexing[idx]
    jump -= 1
    while True:
        length = len(indexing)
        if length == 1:
            answer = [indexing[0][0] + 1, indexing[0][1] + 1]
            break

        if jump < length:
            idx = (idx + jump) % length
            temp_field[indexing[idx][0]][indexing[idx][1]] = temp_cnt
            temp_cnt += 1
            del indexing[idx]
        else:
            t_jump = jump
            t_jump -= length
            idx = (idx + t_jump) % length
            temp_field[indexing[idx][0]][indexing[idx][1]] = temp_cnt
            temp_cnt += 1
            del indexing[idx]

    return answer


print(solution(5, 3))
