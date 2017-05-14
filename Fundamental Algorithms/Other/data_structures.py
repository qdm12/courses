""" STRUCTURES """
class Array:
    """ Access: O(1)
        Search: O(n)
        Insertion: O(n)
        Deletion: O(n)
    """
    def __init__(self):
        self.items = []
        
    def access(self, index): # O(1)
        return self.items[index]
        
    def search(self, item): # O(n)
        for i in self.items:
            if item == i:
                return True
        return False
    
    def insert(self, index, item): # O(n)
        self.items.insert(index, item)

    def delete(self, item): # O(n)
        for i in range(len(self.items)):
            if item == self.items[i]:
                self.items.pop(i)

    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return not self.items

class Stack:
    """ Access: O(n)
        Search: O(n)
        Insertion: O(1)
        Deletion: O(1)
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item) #add to front

    def pop(self):
        return self.items.pop(0) #removes front

    def peek(self): #top of stack
        return self.items[0]

    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return not self.items
    
class Queue:
    """ Access: O(n)
        Search: O(n)
        Insertion: O(1)
        Deletion: O(1)
    """
    def __init__(self):
        self.items = []

    def search(self, item): # O(n)
        for i in self.items:
            if i == item:
                return True
        return False

    def enqueue(self, item): # O(1)
        self.items.insert(0,item) #add to front

    def dequeue(self): # O(1)
        return self.items.pop() #removes last item

    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    
class LinkedList:
    """ Access: O(n)
        Search: O(n)
        Insertion: O(1)
        Deletion: O(1)
    """
    class Node:
        def __init__(self, x, Next=None):
            self.val = x
            self.next = Next
        
    def search(self, head, key):
        # @param head : Head node
        # @param key : Value to be searched
        # @return found : True if found, else False
        while head is not None:
            if head.val == key:
                return True
            head = head.next
        return False
    
    def insert(self, head, key): # O(1)
        # Only inserts at top of linked list
        # @param head : Head node
        # @return New head
        NewNode = self.Node(key)
        if head is None:
            return NewNode
        NewNode.next = head
        return NewNode
    
    def insert_index(self, head, key, pos=0):
        # @param head : Head node
        # @param key : Value to be inserted
        # @param pos : Position at which it has to be inserted
        # @return New head
        NewNode = self.Node(key)
        if head is None:
            return NewNode
        if pos == 0:
            NewNode.next = head
            return NewNode
        A = head
        for _ in range(pos-1):                
            if A.next is None: #we reached the end
                A.next = NewNode
                return head
            A = A.next
        if A.next is None: #we reached the end
            A.next = NewNode
            return head
        NewNode.next = A.next
        A.next = NewNode
        return head
    
    def delete(self, A, key):
        # @param A : Head node
        # @param key : Value to be deleted
        # @return New head
        head = A
        if head.val == key:
            if head.next is None:
                return None
            else:
                return head.next
        while A.next is not None:
            if A.next.val == key:
                A.next = A.next.next #this can be None, it's fine
                return head
            A = A.next

    def print_list(self, A):
        # @param A : Head node
        while A is not None:
            print A.val,
            A = A.next
        print 
    
    # Complexity O(n) and space O(1)
    def print_reverse(self, A):
        # @param A : Head node
        if A is not None:
            self.print_reverse(A.next)
            print A.val,
            
    # Complexity O(n) and space O(1)
    def reverse(self, A):
        # @param A : Head node
        # @return New head
        if A.next is None:
            return A
        rest = self.reverse(A.next)
        A.next.next = A
        A.next = None
        return rest   
    
    # Complexity O(n) and space O(1)
    def clone(self, A):
        # @param A : Head node
        # @return New head
        head = self.Node(A.val)
        newNode = head
        while A.next is not None:
            newNode.next = self.Node(A.next.val)
            newNode = newNode.next
            A = A.next
        return head
    
    def test(self):
        head = self.insert(None, 5)
        head = self.insert(head, 4)
        head = self.insert(head, 3)
        head = self.insert(head, 2)
        head = self.insert_index(head, 1, 3)
        self.print_list(head)
        head = self.delete(head, 1)
        self.print_list(head)
        head = self.reverse(head)
        self.print_list(head)
        self.print_reverse(head)
        
        
class DoublyLinkedList:
    """ Access: O(n)
        Search: O(n)
        Insertion: O(1)
        Deletion: O(1)
    """
    class Node:
        def __init__(self, x, prev=None, Next=None):
            self.val = x
            self.next = Next
            self.prev = prev
            
    def search(self, head, key): # SAME O(n)
        # @param head : Head node
        # @param key : Value to be searched
        # @return found : True if found, else False
        while head is not None:
            if head.val == key:
                return True
            head = head.next
        return False
    
    def insert(self, head, key): # SAME O(1)
        # Only inserts at top of linked list
        # @param head : Head node
        # @return New head
        NewNode = self.Node(key)
        if head is None:
            return NewNode
        NewNode.next = head
        return NewNode
    
    def delete(self, A, key):
        # @param A : Head node
        # @param key : Value to be deleted
        # @return New head
        head = A
        if head.val == key:
            if head.next is None:
                return None
            else:
                return head.next
        while A.next is not None:
            if A.next.val == key:
                A.next = A.next.next #this can be None, it's fine
                if A.next is not None:
                    A.next.prev = A
                return head
            A = A.next

    def print_list(self, A):
        # @param A : Head node
        while A is not None:
            print A.val,
            A = A.next
        print 
    
    # Complexity O(n) and space O(1)
    def print_reverse(self, A):
        # @param A : Head node
        if A is not None:
            self.print_reverse(A.next)
            print A.val,

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
        maxi = A[0]
        A[0] = A[-1]
        del A[-1] #use del so it stays out of the function
        self.max_heapify(A, 0)
        return maxi
        
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
            
class SkipList:
    """ Access: O(log n)
        Search: O(log n)
        Insertion: O(log n)
        Deletion: O(log n)
    """
    
class HashTable:
    """ Access: NA
        Search: O(1)
        Insertion: O(1)
        Deletion: O(1)
    """
    
class BinarySearchTree:
    """ Access: O(log n)
        Search: O(log n)
        Insertion: O(log n)
        Deletion: O(log n)
    """
    class Node(object):
        def __init__(self, key):
            self.val = key
            self.left = None
            self.right = None
        
    def search(self, root, key):    
        if root is None or root.val == key: # root is null or key is present at root
            return root
        if root.val < key: # Key is greater than root's key
            return self.search(root.right, key)
        else: # Key is smaller than root's key
            return self.search(root.left, key)
        return None
        
    def search_iteratively(self, root, key):
        while root is not None:
            if key == root.key:
                return root
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return None
                
    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
                    
    def minValue(self, root):
        while root.left is not None:
            root = root.left    
        return root.val
    
    def minValue_recursive(self, root):
        if root.left is None:
            return root
        else:
            return self.minValue_recursive(root.left)
    
    def maxValue(self, root):
        while root.right is not None:
            root = root.right    
        return root.val
                    
    def leftSuccessor(self, root, parent_key):
        while root.left is not None:
            if root.val == parent_key:
                return root.left
            elif parent_key < root.val:
                return self.leftSuccessor(root.left, parent_key)
            else:
                return self.leftSuccessor(root.right, parent_key)
                    
    def delete(self, root, key):
        if root is None:
            return None
        if root.val == key:
            if root.left is not None and root.right is not None: # 2 childs
                minValue = self.minValue(root.right)
                root.val = minValue
                root.right = self.delete(root.right, minValue)                    
            elif root.left is not None: # only left child
                return root.left
            elif root.right is not None: # only right child
                return root.right
            else: # no child
                return None
        elif root.val < key:
            root.right = self.delete(root.right, key)
        else:
            root.left = self.delete(root.left, key)
        return root               
    
    def isBST(self, node, minKey, maxKey):
        if node is None:
            return True
        if node.val < minKey or node.val > maxKey:
            return False
        return self.isBST(node.left, minKey, node.val - 1) and \
               self.isBST(node.right, node.val + 1, maxKey)

    def print_inOrder(self, root):
        if root:
            self.print_inOrder(root.left)
            print root.val,
            self.print_inOrder(root.right)
            
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def serializeHelper(node, values):
            if node:
                values.append(node.val)
                serializeHelper(node.left, values)
                serializeHelper(node.right, values)
        values = []
        serializeHelper(root, values)
        return ' '.join(map(str, values))
    

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def deserializeHelper(minVal, maxVal, values):
            if not values:
                return None
            if minVal < values[0] < maxVal:
                value = values[0]
                del values[0]
                node = self.Node(value)
                node.left = deserializeHelper(minVal, value, values)
                node.right = deserializeHelper(value, maxVal, values)
                return node
            return None
        values = [int(val) for val in data.split()]
        return deserializeHelper(float('-inf'), float('inf'), values)
            
    def test(self):
        #      50
        #    /    \
        #   30     70
        #   / \    / \
        #  20 40  60 80
        r = self.Node(50)
        self.insert(r, self.Node(30))
        self.insert(r, self.Node(20))
        self.insert(r, self.Node(40))
        self.insert(r, self.Node(70))
        self.insert(r, self.Node(60))
        self.insert(r, self.Node(80))
        self.print_inOrder(r)
        print 
        print 
        r = self.delete(r, 70)
        self.print_inOrder(r)
        
x = BinarySearchTree()
x.test()




