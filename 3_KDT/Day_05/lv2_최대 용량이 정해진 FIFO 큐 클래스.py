#
#  lv2_최대 용량이 정해진 FIFO 큐 클래스.py
#  최대 용량이 정해진 FIFO 큐 클래스
#
#  Create by 김도영 on 2021/04/23
#


class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size()

    def push(self, item):
        if self.qsize() == self.max_size:
            return False

        if self.qsize() == 0:  # 비어있으면
            self.stack1.push(item)

        else:
            while self.qsize() != 0:
                self.stack2.push(self.stack1.pop())

            self.stack1.push(item)
            while self.stack2.size() != 0:
                self.stack1.push(self.stack2.pop())
        return True

    def pop(self):
        try:
            if self.qsize() == 0:  # 비어있으면
                raise EmptyException

            return self.stack1.pop()
        except EmptyException:
            return False


class EmptyException(Exception):
    pass


n, max_size = map(int, input().strip().split(" "))
queue = MyQueue(max_size)
for _ in range(int(n)):
    op = input().strip().split()

    if op[0] == "PUSH":
        print(queue.push(op[1]))
    elif op[0] == "SIZE":
        print(queue.qsize())
    elif op[0] == "POP":
        print(queue.pop())
