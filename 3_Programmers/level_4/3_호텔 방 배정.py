import sys

sys.setrecursionlimit(10000)


def find(x, rooms):
    if x not in rooms:
        rooms[x] = x + 1
        return x

    p = find(rooms[x], rooms)
    rooms[x] = p + 1
    return p


def solution(k, room_number):
    answer = []
    rooms = dict()

    for room in room_number:
        empty = find(room, rooms)
        answer.append(empty)

    return answer
