""" creates a binary search tree """

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f"{self.data}"


class BST:
    def __init__(self):
        pass

    def insert(self, root, node):

           # if there is no root 
        if root is None: 
            root = node
            print(f'{node.data} inserted at root')

        # if the data is less than root search for left node
        else: 
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                    print(f'{node.data} inserted at left')
                else:
                    self.insert(root.left, node)
        
            else:
                if root.right is None:
                    root.right = node
                    print(f'{node.data} inserted at right')
                else:
                    self.insert(root.right, node)

    def inorder(self, root):

        if root is None:
            return
        self.inorder(root.left)
        print(root)
        self.inorder(root.right)
    
    def postorder(self, root):

        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root)
      
    def preorder(self, root):
    
        if root is None:
            return

        print(root)
        self.postorder(root.left)
        self.postorder(root.right)
        


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    # print(n1)
    bst  = BST()
    bst.insert(n1, n2)
    bst.insert(n1, n3)
    bst.insert(n1, n4)
    bst.insert(n1, n5)
    bst.inorder(n1)
    print("*" * 5)
    bst.postorder(n1)
    print("*" * 5)
    bst.preorder(n1)


