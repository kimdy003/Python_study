board = [[0] * 10 for _ in range(10)]
movdir = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 상 좌 하 우
lst, _lst = [], []


def dfs(y, x, cnt, path, visited):
    global lst
    if cnt == 3:
        lst.append(path)
        return

    else:
        for i in range(4):
            ny, nx = y + movdir[i][0], x + movdir[i][1]
            if 0 <= ny < 10 and 0 <= nx < 10:
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    dfs(ny, nx, cnt + 1, path + str(i), visited)
                    visited.remove((ny, nx))


def _dfs(y, x, cnt, path):
    global _lst
    if cnt == 3:
        _lst.append(path)
        return

    else:
        for i in range(4):
            ny, nx = y + movdir[i][0], x + movdir[i][1]
            if 0 <= ny < 10 and 0 <= nx < 10:
                _dfs(ny, nx, cnt + 1, path + str(i))


dfs(5, 5, 0, "", set())
_dfs(5, 5, 0, "")

for _ in range(len(_lst) - len(lst)):
    lst.append("0")
print("lst : {} _lst : {}".format(len(lst), len(_lst)))
for i in zip(lst, _lst):
    print(i)
