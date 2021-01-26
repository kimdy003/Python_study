def solution(tickets):
    dict = {}
    for t in tickets:
        dict[t[0]] = dict.get(t[0], []) + [t[1]]
    
    for d in dict:
        dict[d].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top in dict and dict[top]:
            stack.append(dict[top].pop())
        else:
            path.append(stack.pop())

    return path[::-1]

print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))