def solution(table, languages, preference):
    answer = [[0, "SI"], [0, "CONTENTS"], [0, "HARDWARE"], [0, "PORTAL"], [0, "GAME"]]
    lst = [i for i in zip(languages, preference)]
    
    ans_idx = 0
    for tab in table:
        tab = tab.split()
        dic = {key: 6-idx for idx, key in enumerate(tab)}

        temp = 0
        for l in lst:
            temp += dic.get(l[0], 0) * l[1]

        answer[ans_idx][0] = temp
        ans_idx += 1

    Max, ans = 0, ""   
    for s in answer:
        if Max <= s[0]:
            Max = s[0]
            ans = s[1]

    return ans

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["JAVA", "JAVASCRIPT"], [7, 5]))