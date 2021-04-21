# 
#  lv2_카펫.py
#  lv2_카펫 
#
#  Created by 김도영 on 2021/04/20.
#

def solution(brown, red):
    answer = []
    
    for x in range(1, red+1):
        if not red%x:
            y = red//x
            if ((x+2)*(y+2)) - (x*y) == brown:
                return [max(x+2, y+2), min(x+2, y+2)]