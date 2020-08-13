class Node():
    def __init__(self, key = 0):
        self.data = key
        self.next = None

class Node_Stack():
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, key):
        new_node = Node(key)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def return_top(self):
        if self.is_empty():
            print("empty stack")
            return -1
        else:
            return self.top.data
    
    def pop(self):
        if self.is_empty():
            print("empty stack")
            return -1
        else:
            self.top = self.top.next
    
    def print_as_string(self):
        s = "TOP["
        if self.is_empty():
            s += "]BOTTOM"
        else:
            curr = self.top
            while True:
                s += str(curr.data)
                if curr.next == None:
                    break
                else:
                    s += " "
                curr = curr.next
            s += "]BOTTOM"
        print(s)