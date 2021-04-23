#
#  22강.py
#  최대 힙에 새로운 원소 삽입
#
#  Create by 김도영 on 2021/04/21



class MaxHeap:
    
    def __init__(self):
        self.data = [None]


    def insert(self, item):
        ll = len(self.data)
        self.data.append(item)
        
        while (ll // 2) > 0:
            if self.data[ll//2] < self.data[ll]:
                self.data[ll//2], self.data[ll] = self.data[ll], self.data[ll//2]
            ll //= 2


def solution(x):
    return 0