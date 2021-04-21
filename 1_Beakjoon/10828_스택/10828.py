from sys import stdin

class Stack:
    def __init__(self):
        self.len = 0
        self.list = []
    
    def push(self, num):
        self.list.append(num)
        self.len += 1
    
    def pop(self):
        if(self.size() == 0):
            return -1
        pop_ret = self.list[self.len -1]
        del self.list[self.len -1]
        self.len -= 1
        return pop_ret
    
    def size(self):
        return self.len
    
    def empty(self):
        return 1 if self.len == 0 else 0
    
    def top(self):
        return self.list[-1] if self.len != 0 else -1

num = int(stdin.readline())
stack = Stack()
while(num > 0):
    num -= 1

    input_split = stdin.readline().split()
    order = input_split[0]

    if order == "push":
        stack.push(input_split[1])
    elif order == "pop":
        print(stack.pop())
    elif order == "size":
        print(stack.size())
    elif order == "empty":
        print(stack.empty())
    elif order == "top":
        print(stack.top())