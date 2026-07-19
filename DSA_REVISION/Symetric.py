class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def Is_Symmetric(self,root):
        if root is None:
            return 

        def Mirror(left,right):
            

            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val!=right.val:
                return False

            return Mirror(left.left,right.right) and Mirror(left.right,right.left)

        

        return Mirror(root.left,root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(6)
root.left.right = TreeNode(5)

print(root.Is_Symmetric(root))
