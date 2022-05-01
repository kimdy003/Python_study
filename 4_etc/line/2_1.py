import re

def solution(program, flag_rules, commands):
    answer = []
    
    rule = {}
    # flag_rules의 데이터를 공백을 기준으로 split해주고 rule 배열에 저장했습니다.
    for flag_rule in flag_rules:
        flag_rule = flag_rule.split()
        rule[flag_rule[0]] = flag_rule[1]

    #각 commands마다 rule에 저장된 규칙으로 판별합니다
    for command in commands:
        command = command.split()
        if command[0] != program:
            answer.append(False)
            break

        i = 1
        flag = True
        while i != len(command):
            if command[i] not in rule:
                answer.append(False)
                flag = False
                break
            
            if i+1 < len(command):
                if rule[command[i]] == "STRING":
                    #알파벳 대소문자만
                    p = re.compile('[a-zA-Z]+')
                    if p.match(command[i+1]) == None:
                        answer.append(False)
                        flag = False
                        break
                    i += 2

                elif rule[command[i]] == "NUMBER":
                    p = re.compile('[0-9]+')
                    if p.match(command[i+1]) == None:
                        answer.append(False)
                        flag = False
                        break
                    i += 2

                elif rule[command[i]] == "NULL":
                    if command[i+1] not in rule:
                        answer.append(False)
                        flag = False
                        break
                    
                    i += 1
            else:
                if rule[command[i]] != "NULL":
                    answer.append(False)
                    flag = False
                    break
                i += 1

        if flag == True:
            answer.append(True)

    return answer

solution("line",["-s STRING", "-n NUMBER", "-e NULL"],["line -s 123 -n HI", "line fun"])