def solution(S):
    answer = []

    for s in S:
        temp = ""
        stack = []
        for c in s:
            if c == "0":
                if stack[-2:] == ["1", "1"]:
                    stack.pop()
                    stack.pop()
                    temp += "110"
                else:
                    stack.append(c)
            else:
                stack.append(c)

        if len(temp) == 0:
            answer.append(s)
        else:
            stack = "".join(stack)
            point = len(stack)
            for i in range(len(stack) - 1, -1, -1):
                if stack[i] == "1":
                    point = i
                else:
                    break

            answer.append(stack[:point] + temp + stack[point:])

    return answer


print(solution(["1110", "100111100", "0111111010"]))
