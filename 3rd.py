class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root



root = None
root = insert(root, 15)
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 12)
root = insert(root, 16)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 12")
root = deleteNode(root, 12)

print("Inorder traversal of the modified tree")
inorder(root)
