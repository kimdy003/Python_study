import re
import math

def solution(str1, str2):
    answer = 0

    list_1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    list_2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
    
    inter = set(list_1) & set(list_2)
    union = set(list_1) | set(list_2)
    
    if len(union) == 0:
        return 65536
    
    inter_sum = sum([min(list_1.count(s), list_2.count(s)) for s in inter])
    union_sum = sum([max(list_1.count(s), list_2.count(s)) for s in union])

    return math.floor((inter_sum/union_sum)*65536)