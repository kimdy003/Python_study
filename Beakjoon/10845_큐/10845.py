from sys import stdin

class Queue:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, data):
        self.list.append(data)
        self.len += 1

    def pop(self):
        if not self.len:
            return -1

        pop_num = self.list[0]
        del self.list[0]
        self.len -= 1
        return pop_num

    
    def size(self):
        return self.len
    
    def empty(self):
        if not self.len:
            return 1
        return 0
    
    def front(self):
        if not self.len:
            return -1
        
        return self.list[0]
    
    def back(self):
        if not self.len:
            return -1
        
        return self.list[-1]

T = int(stdin.readline())
queue = Queue()
for _ in range(T):
    input =  stdin.readline().split()

    if input[0] == "push":
        queue.push(input[1])

    elif input[0] == "pop":
        print(queue.pop())

    elif input[0] == "size":
        print(queue.size())

    elif input[0] == "empty":
        print(queue.empty())

    elif input[0] == "front":
        print(queue.front())

    elif input[0] == "back":
        print(queue.back())