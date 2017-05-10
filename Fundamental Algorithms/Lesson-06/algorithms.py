class BinarySearchTree:
    class Node(object):
        def __init__(self, key):
            self.val = key
            self.left = None
            self.right = None
            
    def SuccessorVerbose(self, root, parent_key):
        while root.left is not None:
            if root.val == parent_key:
                print "Parent found and has left successor", root.left.val
                return root.left
            elif parent_key < root.val:
                print "Parent's value is on left side of node", root.val
                return self.SuccessorVerbose(root.left, parent_key)
            else:
                print "Parent's value is on right side of node", root.val
                return self.SuccessorVerbose(root.right, parent_key)
        print "No successor found."
        
    def minValueVerbose(self, root):
        while root.left is not None:
            print "There is a node on the left of node with value", root.val
            root = root.left    
        print "No more node on the left of node with value", root.val
        print "The minimum is therefore the node with value", root.val
        return root.val
    
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
                    
    def print_inOrder(self, root):
        if root:
            self.print_inOrder(root.left)
            print root.val,
            self.print_inOrder(root.right)
            
    def run(self):            
        root = self.Node(80)
        self.insert(root, self.Node(70))
        self.insert(root, self.Node(200))
        self.insert(root, self.Node(150))
        self.insert(root, self.Node(140))
        self.insert(root, self.Node(170))
        self.insert(root, self.Node(148))
        self.insert(root, self.Node(143))
        self.SuccessorVerbose(root, 150)
        self.minValueVerbose(root)
        print
        self.print_inOrder(root)
        print
        self.delete(root, 140)
        self.print_inOrder(root)

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

