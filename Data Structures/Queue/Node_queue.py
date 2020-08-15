class Node():
    def __init__(self, key = 0):
        self.data = key
        self.next = None

class Node_Queue():
    def __init__(self):
        self.top = None
        self.bottom = None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, key):
        new_node = Node(key)
        if self.is_empty:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        
    def return_top(self, key):
        if self.is_empty():
            print("empty queue")
            return -1
        else:
            return self.top.data
    
    def return_bottom(self, key):
        if self.is_empty():
            print("empty queue")
            return -1
        else:
            return self.bottom.data

    def pop(self):
        if self.is_empty():
            print("empty queue")
            return -1
        else:
            curr = self.top
            
    def print_as_string(self):
        s = "["
        if not self.is_empty():
            curr = self.top
            
            while True:
                s += str(curr.data)
                if curr.next == None:
                    break
                
                s += " "
                curr = curr.next

        s+="]BOTTOM"
        print(s)
            
"""
수ㅡ정필요함
"""