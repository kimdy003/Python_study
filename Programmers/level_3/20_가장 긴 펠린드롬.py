def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i, len(s)+1):

            def check(str):
                return str == str[::-1]

            if check(s[i:j]):
                answer = max(answer, len(s[i:j]))

    return answer
    
print(solution("abcdcba"))