RED = 1
BLACK = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = BLACK
        self.root = self.NIL

    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        temp = self.root

        while temp != self.NIL:
            parent = temp
            if node.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        node.color = RED
        self.fix_insert(node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
        self.root.color = BLACK

    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


# Driver Code
rb = RedBlackTree()
rb.insert(55)
rb.insert(40)
rb.insert(65)
rb.insert(60)
rb.insert(75)
rb.insert(57)

print("Inorder traversal of Red Black Tree:")
rb.inorder(rb.root)
