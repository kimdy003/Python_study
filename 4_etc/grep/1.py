user_ = [False, False]  # [0] false : Login 안함 , [1] false : 장바구니가 비어있음

def ADD(act):
    global user_
    if user_[0] == False:
        return False
    
    user_[1] = True
    return True

def LOGIN(act, dic_info):
    global user_
    if act[1] not in dic_info:
        return False
    
    if user_[0] == True or dic_info[act[1]] != act[2]:
        return False
    
    user_[0] = True
    return True

def ORDER(act):
    global user_
    if user_[1] == False:
        return False
    
    user_[1] = False
    return True

def solution(infos, actions):
    answer = []
    dic_info = {}
    for info in infos:
        key, val = info.split()
        dic_info[key] = val
    
    for action in actions:
        act = action.split()
        
        if act[0] == 'ADD':
            answer.append(ADD(act))
            
        elif act[0] == 'LOGIN':
            answer.append(LOGIN(act, dic_info))
            
        elif act[0] == 'ORDER':
            answer.append(ORDER(act))
            
    return answer