def solution(operations):
    queue = []

    for operation in operations:
        flag, num = operation.split(" ")
        num = int(num)
        if flag == "I":
            queue.append(num)
            
        elif queue:
            if num == 1:
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
        
    if queue:
        return [max(queue), min(queue)]
    else:
        return [0, 0]

print(solution(["I 7","I 5","I -5","D -1"]))