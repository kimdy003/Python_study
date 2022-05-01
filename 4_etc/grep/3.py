def check(visit, row, col):
    for r in range(row):
        v = visit[r]

        if col == v:
            return False

    return True


def Place(word, cards, visit, exist, row):
    # 끝내는 조건 추가
    for w in word:
        if len(exist[w]) != 0:
            break
    else:
        return 1

    cnt = 0
    for col in range(len(cards[0])):
        if check(visit, row, col) == True:
            # cards에서 word에 있는 단어 col넣기
            if cards[row][col] in exist:
                if len(exist[cards[row][col]]) != 0:
                    temp = exist[cards[row][col]].pop()
                    visit[row] = col
                    cnt += Place(word, cards, visit, exist, row + 1)

                    exist[cards[row][col]].append(temp)

    return cnt


def solution(word, cards):
    answer = 0
    exist = {}
    for i, w in enumerate(word):
        exist[w] = exist.get(w, []) + [i]

    num = len(cards) - len(word)
    for row in range(num + 1):
        visit = [0] * len(cards[row:])
        answer += Place(word, cards[row:], visit, exist, 0)

    return answer


print(solution("BAB", ["ZZBZ", "BAZB", "XBXB", "XBAX"]))
