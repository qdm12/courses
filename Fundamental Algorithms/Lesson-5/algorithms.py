from string import ascii_uppercase        

class HashingChaining(object):
    def __init__(self):
        self.hashtable = [[] for _ in range(7)]
        
    def hash(self, key): #key is in the form 'ABCD' in capitals
        sum = 0
        for C in key:
            sum += ascii_uppercase.find(C) + 1
        digest = sum % 7
        return digest
        
    def insert(self, key):
        index = self.hash(key)
        self.hashtable[index].insert(0, key)
        
    def search(self, key):
        index = self.hash(key)
        for sub_index in range(len(self.hashtable[index])):
            if key == self.hashtable[index][sub_index]:
                return index, sub_index
        return -1, -1
        
    def delete(self, key):
        index, sub_index = self.search(key)
        if index != -1: #key was found
            del self.hashtable[index][sub_index]
            
    def print_hashtable(self):
        print "Index Key"
        for i in range(7):
            print i, "   ", self.hashtable[i]
            
    def run(self):
        self.print_hashtable()
        self.insert("COBB")
        self.print_hashtable()
        self.insert("RUTH")
        self.print_hashtable()
        self.insert("ROSE")
        self.print_hashtable()
        self.search("BUZ")
        self.insert("DOC")
        self.print_hashtable()
        self.delete("COBB")
        self.print_hashtable()

class MergeSort(object):
    def merge(self, L, R):
        C = []
        i, j = 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                C.append(L[i])
                i += 1
            else:
                C.append(R[j])
                j += 1
        while i < len(L):
            C.append(L[i])
            i += 1
        while j < len(R):
            C.append(R[j])
            j += 1
        return C

    def mergeSort(self, A):
        if len(A) < 2:
            return A
        else:
            middle = len(A) / 2
            L = mergeSort(A[:middle])
            R = mergeSort(A[middle:])
            return merge(L, R)
            
    def run(self):
        A = [54,26,93,17,77,31,44,55,20]
        print mergeSort(A)        
        
class BinarySearchTree(object):
    class Node(object):
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key
        
    def search(self, root, key):    
        if root is None or root.val == key: # root is null or key is present at root
            return root
        if root.val < key: # Key is greater than root's key
            return search(root.right, key)
        else: # Key is smaller than root's key
            return search(root.left, key)
            
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
                    
    def insert_verbose(self, root, node):
        if root is None:
            print "  No node, attributing new node here."
            root = node
        else:
            if root.val < node.val:
                print "New node has key",node.val,">",root.val,"(current node)"
                print "Checking the right side of node with key", root.val
                if root.right is None:
                    print "  No node at right side, attributing new node here"
                    root.right = node
                else:
                    self.insert_verbose(root.right, node)
            else:
                print "New node has key",node.val,"<",root.val,"(current node)"
                print "Checking the right side of node, with key", root.val
                if root.left is None:
                    print "  No node at left side, attributing new node here"
                    root.left = node
                else:
                    self.insert_verbose(root.left, node)

    def delete(self):
        pass

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
            
    def run(self):
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
        self.inorder(r)