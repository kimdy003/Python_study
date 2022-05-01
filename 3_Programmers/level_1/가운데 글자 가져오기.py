#가운데 글자 가져오기

def solution(s):
    answer = ''
    p = len(s)//2
    #홀수
    if len(s)%2:
        return s[p]
    else:
        return s[p-1:p+1]