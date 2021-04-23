#
#  3_여행경로.py
#  여행경로
#
#  Create by 김도영 on 2021/04/23
#


def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())

    return path[::-1]
