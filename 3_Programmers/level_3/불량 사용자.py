import re
from itertools import permutations


def isMatch(user, ban_id):
    for i in range(len(ban_id)):
        p = re.compile(ban_id[i])
        if not p.match(user[i]) or len(user[i]) != len(ban_id[i]):
            return False
    return True


def solution(user_id, banned_id):
    answer = []
    N = len(banned_id)
    banned_id = [ban.replace("*", ".") for ban in banned_id]

    for perm in permutations(user_id, N):
        if isMatch(perm, banned_id):
            perm = sorted(list(perm))  # perm = set(perm)
            if perm not in answer:
                answer.append(perm)
    print(answer)
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))

for i in [("a", "b", "c"), ("b", "c", "a"), ("b", "a", "c"), ("c", "a", "b"), ("a", "b", "c")]:
    print(set(i))
