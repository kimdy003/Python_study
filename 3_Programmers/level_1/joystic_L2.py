#조이스틱

def solution(name):
    name_list = [min(ord(i) - ord('A'), ord('Z') - ord(i)+1) for i in name]
    idx, ans= 0, 0
    while True:
        ans += name_list[idx]
        name_list[idx] = 0
        if sum(name_list) == 0:
            break
            
        left, right = 1, 1
        while name_list[idx - left] ==0:
            left +=1
        while name_list[idx + right] ==0:
            right +=1
        ans += left if left < right else right
        idx += -left if left < right else right
    return ans

print(solution("JESON"))