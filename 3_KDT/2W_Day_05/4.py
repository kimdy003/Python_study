from itertools import permutations


def calculation(nums, oper):
    stack = [nums[0]]

    for i in range(len(oper)):
        top = stack.pop()
        if oper[i] == "+":
            top += nums[i + 1]
            stack.append(top)
        else:
            top -= nums[i + 1]
            stack.append(top)

    return stack[-1]


def solution(arr):
    answer = -987654321
    nums, oper = [], []
    for a in arr:
        if a == "+" or a == "-":
            oper.append(a)
        else:
            nums.append(int(a))

    return answer


print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))