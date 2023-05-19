def solution(s):
    words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    ans, temp = "", ""

    for w in s:
        if w.isdigit():
            ans += w
        else:
            temp += w
            if temp in words:
                ans += words[temp]
                temp = ""

    return ans


print(solution("one4seveneight"))
