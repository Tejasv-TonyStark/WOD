class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def Diameter(self,root):
       
        self.diameter = 0

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.diameter = max(self.diameter,left+right)

            return 1+max(left,right)
        height(root)


        return self.diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(6)
root.left.right = TreeNode(5)

print(root.Diameter(root))



