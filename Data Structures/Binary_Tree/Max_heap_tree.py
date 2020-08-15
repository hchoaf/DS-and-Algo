class Max_Heap_Tree():
    def __init__(self):
        self.heap_list = list()
    
    def get_max(self):
        #returns maximum value in heap tree
        assert len(self.heap_list) != 0, "empty heap"
        return self.heap_list[0]

    
    def return_parent(self, index):
        #returns parent index of an index
        assert index != 0, "root element doesn't have any parent"
        return int(index/2)

    def return_left_child(self, index):
        #returns left child index of an index
        return int(2*index)

    def return_right_child(self, index):
        #returns right child index of an index
        return int(2*index + 1)

    def sift_up(self, index):
        # swap element in index with parent element until none of its parents has smaller priority than the element
        while index > 0 and self.heap_list[self.return_parent(index)] < self.heap_list[index]:
            self.heap_list[self.return_parent(index)], self.heap_list[index] = self.heap_list[index], self.heap_list[self.return_parent(index)]
            index = self.return_parent(index)
        
    def sift_down(self, index):
        # swap element in index with max(leftchild, rightchild) until none of its children has larger priority than the element
        max_index = index
        l_index = self.return_left_child(index)
        if l_index < len(self.heap_list) and self.heap_list[l_index] > self.heap_list[max_index]:
            max_index = l_index
        r_index = self.return_right_child(index)
        if r_index < len(self.heap_list) and self.heap_list[r_index] > self.heap_list[max_index]:
            max_index = r_index
        
        if index != max_index:
            self.heap_list[index], self.heap_list[max_index] = self.heap_list[max_index], self.heap_list[index]
            self.sift_down(max_index)

        

    def insert(self, key):
        # insert an element with priority = key
        self.heap_list.append(key)
        self.sift_up(len(self.heap_list)-1)

    def extract_max(self):
        # extracts an element with the maximum priority from heap tree
        return_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop()
        self.sift_down(0)
        return return_val

    def height(self):
        # returns height of heap tree
        counter = 0
        number = len(self.heap_list)
        while number >= 1:
            number = int(number/2)
            counter += 1
        return counter


    def print_tree(self):
        # prints heap tree
        print("Tree")
        assert len(self.heap_list) != 0, "Empty heap"
        levels = [pow(2, i)-1 for i in range(1, self.height()+1)]
        it = 0
        for i in range(len(self.heap_list)):
            print(self.heap_list[i], end = ' ')
            if i >= levels[it]-1:
                print('\n')
                it += 1
        print("\n")


    def remove(self, index):
        # removes an element in index = index from heap tree
        self.heap_list[index] = pow(2, 20) # infinity
        self.sift_up(index)
        self.extract_max()

    def change_priority(self, index, new_priority):
        # replace priority of element in index=index with new_priority
        old_priority = self.heap_list[index]
        self.heap_list[index] = new_priority
        if new_priority > old_priority:
            self.sift_up(index)
        else:
            self.sift_down(index)


tree = Max_Heap_Tree()
for i in range(1, 12):
    tree.insert(i)

tree.print_tree()
for i in range(1, 12):
        
    tree.extract_max()
    tree.print_tree()