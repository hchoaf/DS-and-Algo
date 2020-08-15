class Max_Heap_Tree():
    def __init__(self):
        self.heap_list = list()
        
    
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
        
        if len(self.heap_list) == 1:
            return self.heap_list[0]
        return_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop()
        self.sift_down(0)
        return return_val

def heap_sort_descending(Array):
    new_heap = Max_Heap_Tree()
    for items in Array:
        new_heap.insert(items)
    for i in range(len(Array)):
        Array[i] = new_heap.extract_max()
    return Array

