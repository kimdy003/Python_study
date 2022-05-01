from collections import deque


# character : 체력, 공격력, 방어력
# monsters : 이름(대소문자 구분), 경험치, 체력, 공격력, 방어력
def solution(character, monsters):
    answer = ""
    character = list(map(int, character.split()))
    cand = []

    def bfs():
        queue = deque()
        for idx, monster in enumerate(monsters):
            lst = list(monster.split())
            queue.append(
                [idx, lst[0]] + list(map(int, lst[1:])) + [1] + [character[:]]
            )

        while queue:
            idx, name, cost, hp, attack, shild, time, player = queue.popleft()
            player_attack = player[1] - shild if player[1] - shild > 0 else 0
            monster_attack = attack - player[2] if attack - player[2] > 0 else 0

            # 무한 회귀 확인
            if player_attack <= 0 and monster_attack < player[0]:
                continue

            # step 1. 플레이어 공격
            hp -= player_attack

            # step 2. 몬스터 체력 0이하
            if hp <= 0:
                temp = cost / time
                cand.append([temp, cost, idx, name])
                continue

            # step 3. 몬스터 공격
            player[0] -= monster_attack
            if player[0] > 0:
                player[0] += monster_attack
                queue.append(
                    [idx, name, cost, hp, attack, shild, time + 1, player]
                )

    bfs()
    cand.sort(key=lambda x: [-x[0], -x[1], x[2]])
    return cand[0][-1]


print(
    solution(
        "10 5 2", ["Knight 3 10 10 3", "Wizard 5 10 15 1", "Beginner 1 1 15 1"]
    )
)
