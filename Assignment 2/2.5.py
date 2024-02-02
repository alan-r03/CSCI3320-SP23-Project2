class TreeNode:
    def __init__(self, data = None):
        """
        creates an unallocated node

        :param data: node value
        """
        self.data = data
        self.left = None
        self.right = None

def getPaths(node, allPaths = []):
    """
    finds and returns all depth-first
    paths of the leaves of the root

    :param node: root Node
    :param allPaths: array of all paths
    :return: allPaths
    """
    def depthSearch(node, path = ''):
        """
        searches the tree from the root to the
        leaves and appends the path to allPaths

        :param node: current Node
        :param path: current Node path
        :return: None
        """
        if node == None:
            return path

        path += str(node.data)
        if node.left == None and node.right == None and path != 'None':
            allPaths.append('->'.join(path))

        depthSearch(node.left, path)
        depthSearch(node.right, path)

    depthSearch(node)
    return allPaths

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

print(getPaths(root))