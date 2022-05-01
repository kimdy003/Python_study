'''
2021.10.21
1043_거짓말
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
know_person = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(M)]

person = [0] * N
for know in know_person:
    person[know - 1] = 1

party_true = [0] * M

while know_person:
    know = know_person.pop()
    cands = set()

    for i in range(len(party)):
        if know in party[i]:
            cands = cands.union(set(party[i]))
            party_true[i] = 1

    for cand in cands:
        if not person[cand - 1]:
            person[cand - 1] = 1
            know_person.append(cand)

print(party_true.count(0))
