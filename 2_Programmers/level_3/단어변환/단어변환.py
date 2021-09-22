ans = 987654321

def DFS(begin, visit, words, target, cnt):
    if ''.join(begin) == target:
        global ans
        ans = min(ans, cnt)
        return

    for idx, word in enumerate(words):
        if idx in visit: continue
        if len(word) != len(begin): continue
        
        diff = 0
        for b,w in zip(begin, word):
            if b != w:
                diff += 1

        if diff == 1:
            visit.append(idx)
            DFS(word, visit, words, target, cnt+1)
            visit.pop()


def solution(begin, target, words):
    global ans
    if target not in words:
        return 0

    begin = list(begin)
    words = [list(word) for word in words]
    visit = []

    DFS(begin, visit, words, target, 0)

    if ans == 987654321:
        return 0
    return ans

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))