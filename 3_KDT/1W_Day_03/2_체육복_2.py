#
#  2_체육복_2.py
#  체육복
#
#  Create by 김도영 on 2021/04/22
#

def solutiono(n, lost, reserve):
    s = set(lost) & set(reserve)    # 여분의 체육복을 가져왔지만 도난당한 사람들 (교집합)
    l = set(lost) - s    # 도난당해서 빌려야 되는 학생
    r = set(reserve) - s    # 빌려줄 수 있는 학생
    
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
                
    return n - len(l)