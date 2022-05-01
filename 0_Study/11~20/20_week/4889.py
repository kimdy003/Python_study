import sys

input = sys.stdin.readline
flag = 1
while True:
    _input = list(input().strip())
    if _input[0] == "-":
        break

    stack = []
    ans = 0

    for arr in _input:
        if not stack:
            if arr == "}":
                ans += 1
                stack.append("{")
            else:
                stack.append(arr)

        else:
            if stack[-1] == "{" and arr == "}":
                stack.pop()
            elif arr == "{":
                stack.append(arr)

    print("{}. {}".format(flag, ans + (len(stack) // 2)))
    flag += 1
