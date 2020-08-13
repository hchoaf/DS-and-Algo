class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, key):
        self.stack.append(key)

    def pop(self):
        if self.is_empty():
            print("empty stack")
            return -1
        else:
            self.stack.pop()

    def top(self):
        if self.is_empty():
            print("empty stack")
            return -1
        else:
            return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def print_as_string(self):
        s = "BOT["
        if self.is_empty():
            s += "]TOP"
            print(s)
            return
        else:
            for i in range(len(self.stack)):
                s += str(self.stack[i])
                if i == len(self.stack) - 1:
                    continue
                s += " "
            s += "]TOP"
            print(s)
            return
