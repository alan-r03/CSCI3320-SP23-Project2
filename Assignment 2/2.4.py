class TreeNode:
    def __init__(self, data = None):
        """
        creates an unallocated node

        :param data: node value
        """
        self.data = data
        self.left = None
        self.right = None

    def bstInsert(self, data = None):
        """
        uses the BST properties to
        insert a new integer node

        :param data: new node value
        :return: None
        """
        try:
            data = int(data)
            if self.data == None:
                self.data = data
            else:
                if self.data < data:
                    if self.right == None:
                        self.right = TreeNode(data)
                    else:
                        self.right.bstInsert(data)
                elif self.data > data:
                    if self.left == None:
                        self.left = TreeNode(data)
                    else:
                        self.left.bstInsert(data)
        except:
            pass

def printLevel(node, level):
    """
    prints all nodes on the current
    level from left to right

    :param node: current Node
    :param level: current level
    :return: None
    """
    if node == None:
        return
    if level == 1:
        print([node.data], end=", ")
    else:
        printLevel(node.left, level-1)
        printLevel(node.right, level-1)

def findHeight(node):
    """
    finds the height of the
    binary tree

    :param node: current Node
    :return: height of tree
    """
    if node == None:
        return 0
    leftHeight = findHeight(node.left)
    rightHeight = findHeight(node.right)
    if leftHeight > rightHeight:
        return leftHeight + 1
    else:
        return rightHeight + 1

def printLevelOrder(root):
    """
    prints the level order traversal
    of all nodes in the binary tree

    :param root: tree root
    :return: None
    """
    print("Level order: ", end="")
    height = findHeight(root)
    for level in range(1, height + 1):
        printLevel(root, level)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

printLevelOrder(root)