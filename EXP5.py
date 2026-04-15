import sys

class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(str(node.item) + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(str(node.item) + " ")
            self.in_order_helper(node.right)

    def post_order_helper(self, node):
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(str(node.item) + " ")

    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)

        return self.search_tree_helper(node.right, key)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == None:
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

        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent.color == 1:

            if k.parent == k.parent.parent.right:

                u = k.parent.parent.left

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent

                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)

                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)

            else:

                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent

                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)

                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = 0

    def insert(self, key):

        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x

            if node.item < x.item:
                x = x.left

            else:
                x = x.right

        node.parent = y

        if y == None:
            self.root = node

        elif node.item < y.item:
            y.left = node

        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def rb_transplant(self, u, v):

        if u.parent == None:
            self.root = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        v.parent = u.parent

    def delete_node_helper(self, node, key):

        z = self.TNULL

        while node != self.TNULL:

            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right

            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color

        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)

        elif z.right == self.TNULL:
            x = z.left
            self.rb_transplant(z, z.left)

        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y

            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    def print_helper(self, node, indent, last):

        if node != self.TNULL:

            sys.stdout.write(indent)

            if last:
                sys.stdout.write("R----")
                indent += "     "

            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")

            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)

    def print_tree(self):
        self.print_helper(self.root, "", True)


if __name__ == "__main__":

    bst = RedBlackTree()

    bst.insert(55)
    bst.insert(40)
    bst.insert(65)
    bst.insert(60)
    bst.insert(75)
    bst.insert(57)

    bst.print_tree()

    print("\nAfter deleting an element")
    bst.delete_node(40)

    bst.print_tree()
