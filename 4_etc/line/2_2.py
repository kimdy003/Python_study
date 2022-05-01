import re

def solution(program, flag_rules, commands):
    answer = []
    
    rule = {}
    alias1, alias2 = [], []
    # flag_rules의 데이터를 공백을 기준으로 split해주고 rule 배열에 저장했습니다.
    for flag_rule in flag_rules:
        flag_rule = flag_rule.split()
        if len(flag_rule) == 2:
            rule[flag_rule[0]] = flag_rule[1]
        else:
            rule[flag_rule[0]] = flag_rule[2]
            alias1.append(flag_rule[0])
            alias2.append(flag_rule[2])

    #각 commands마다 rule에 저장된 규칙으로 판별합니다
    for command in commands:
        command = command.split()
        if command[0] != program:
            answer.append(False)
            continue

        i = 1
        flag = True
        alias1_flag, alias2_flag = False, False
        while i != len(command):
            if command[i] not in rule:
                answer.append(False)
                flag = False
                break
            
            if command[i] in alias1:
                alias1_flag = True
            if command[i] in alias2:
                alias2_flag = True

            if alias1_flag and alias2_flag:
                answer.append(False)
                flag = False
                break

            order = command[i]
            while order in rule:
                order = rule.get(order, order)
                
            if i+1 < len(command):
                if order == "STRING":
                    #알파벳 대소문자만
                    p = re.compile('[a-zA-Z]+')
                    if p.match(command[i+1]) == None:
                        answer.append(False)
                        flag = False
                        break
                    i += 2

                elif order == "NUMBER":
                    p = re.compile('[0-9]+')
                    if p.match(command[i+1]) == None:
                        answer.append(False)
                        flag = False
                        break
                    i += 2

                elif order == "NULL":
                    if command[i+1] not in rule:
                        answer.append(False)
                        flag = False
                        break
                    i += 1

                elif order == "STRINGS":
                    p = re.compile('[a-zA-Z]+')
                    while  i+1 < len(command) and command[i+1] not in rule:
                        if p.match(command[i+1]) == None:
                            answer.append(False)
                            flag = False
                            break;
                        i+=1
                    if not flag:
                        break
                    i += 1
                
                elif order == "NUMBERS":
                    p = re.compile('[0-9]+')
                    while i+1 < len(command) and command[i+1] not in rule:
                        if p.match(command[i+1]) == None:
                            answer.append(False)
                            flag = False
                            break
                        i+=1
                    if not flag:
                        break
                    i += 1
            else:
                if order != "NULL":
                    answer.append(False)
                    flag = False
                    break
                i += 1

        if flag == True:
            answer.append(True)

    return answer


print(solution("line",["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],	["line -n 100 -e -num 150"]))
print(solution("bank",["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"],	["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))