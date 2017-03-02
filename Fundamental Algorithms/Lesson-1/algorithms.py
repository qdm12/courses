class Heap(object):
    def parent(self, A, i):
        """ Returns the index in A of the parent of i
            Running time O(1)
            
            Args:
                A (list): Heap
                i (int): Array index
        """
        if i == 0:
            return None
        div = float(i)/2
        if div.is_integer():
            div -= 1
        return int(div)
    
    def right(self, A, i):
        """ Returns the index in A of the right child of i
            Running time O(1)
            
            Args:
                A (list): Heap
                i (int): Array index
        """
        if 2*i + 1 +1 < len(A):
            return 2*i + 1 +1
        return None
    
    def left(self, A, i):
        """ Returns the index in A of the left child of i
            Running time O(1)
            
            Args:
                A (list): Heap
                i (int): Array index
        """
        if 2*i +1 < len(A):
            return 2*i +1
        return None

    def max_heapify(self, A, i):
        """ Outputs A modified so that i roots as heap
            Running time O(log n) where n = len(A) - i
            
            Args:
                A (list): Left and right children of i root heaps (but i may not)
                i (int): Array index
        """
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left < len(A) and A[left] > A[largest]:
            largest = left
        if right < len(A) and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)

    def build_max_heap(self, A):
        """ Outputs A modified to represent a heap
            Running time O(n) where n = len(A)
            
            Args:
                A (list): Unsorted array
                i (int): Array index
        """
        for i in range(len(A)/2, -1, -1):
            self.max_heapify(A, i)

    def heap_increase_key(self, A, i, key):
        """ Outputs A where A[i]'s key was increased to key
            Running time O(log n) where n = len(A)
            
            Args:
                A (list): Heap
                i (int): Array index
                key (int, float): A new key greater than A[i] 
        """
        if key < A[i]:
            raise Exception("New key must be greater than current key")
        A[i] = key
        while i > 0 and A[self.parent(A, i)] < A[i]:
            A[i], A[self.parent(A, i)] = A[self.parent(A, i)], A[i]
            i = self.parent(A, i)
            
    def heap_sort(self, A):
        """ Outputs A sorted from smallest to largest
            Running time O(n log n) where n = len(A)
            
            Args:
                A (list): Unsorted array
        """
        pass
            
    def heap_extract_max(self, A):
        """ Returnrs the max of A and modifies A as a heap with this element removed
            Running time O(log n) where n = len(A)
            
            Args:
                A (list): Heap
            Returns:
                max (int, float): Max element of input Heap tree
        """
        max = A[0]
        A[0] = A[len(A)-1]
        del A[-1] #use del so it stays out of the function
        self.max_heapify(A, 0)
        return max
        
    def max_heap_insert(self, A, key):
        """ Modifies A to include the new key
            Running time O(log n) where n = len(A)
            
            Args:
                A (list): Heap
                key (int, float): Key to insert
        """
        A.append(-9999999)
        self.heap_increase_key(A, len(A)-1, key)
        
    def ptree(self, A, i=0, indent=0):
        if i < len(A):
            print '  ' * indent, A[i]
            self.ptree(A, i * 2 + 1, indent + 1)
            self.ptree(A, i * 2 + 2, indent + 1)
            
    def run(self):
        A = [1, 4, 6, 19, 12, 7]
        self.build_max_heap(A)
        self.ptree(A)
        self.heap_increase_key(A, 2, 8)
        self.ptree(A)
            
if __name__ == "__main__":
    h = Heap()
    h.run()