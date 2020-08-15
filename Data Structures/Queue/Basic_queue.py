class Queue():
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def push(self, key):
        self.queue.insert(0, key)
    
    def top(self):
        if self.is_empty():
            print("empty queue")
            return -1
        else:
            return self.queue[0]

    def pop(self):
        if self.is_empty():
            print("empty queue")
            return -1
        else:
            self.queue.pop()

    def print_as_string(self):
        s = "TOP["
        for i in range(len(self.queue)):
            s += str(self.queue[i])
            if i == len(self.queue) - 1:
                continue
            s += " "
        s += "]BOTTOM"
        print(s)

            
