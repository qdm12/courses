class MergeSort(object):
    def __init__(self):
        self.A = [54,26,93,17,77,31,44,55,20]

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
        print mergeSort(self.A)
        
        
class BinarySearchTree(object):
    def __init__(self):
        pass
        
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