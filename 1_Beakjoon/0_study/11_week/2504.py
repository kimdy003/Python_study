import sys

input = sys.stdin.readline

if __name__ == "__main__":
    stack = []

    arr = list(input().strip())

    for a in arr:
        if a == ")":
            temp = 0
            if not stack:
                print(0)
                exit(0)

            while stack:
                top = stack.pop()
                if top == "(":
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * temp)
                    break
                elif top == "[":
                    print(0)
                    exit(0)
                else:
                    temp += int(top)

        elif a == "]":
            temp = 0
            if not stack:
                print(0)
                exit(0)

            while stack:
                top = stack.pop()
                if top == "[":
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * temp)
                    break
                elif top == "(":
                    print(0)
                    exit(0)
                else:
                    temp += int(top)
        else:
            stack.append(a)

    ans = 0
    for a in stack:
        if a in ["(", ")", "[", "]"]:
            print(0)
            exit(0)
        else:
            ans += a

    print(ans)
