from Node_queue import Node_Queue

queue = Node_Queue()

for i in range(0, 10):
    queue.push(i)
    queue.print_as_string()