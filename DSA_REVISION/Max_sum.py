class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def Max_path_sum(self,root):
        self.max_sum = -float('inf')
        if root is None:
            return 0

        def dfs(node):
            if node is None:
                return 0 

            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
            curr_sum = node.val+left+right

            self.max_sum = max(self.max_sum,curr_sum)

            return node.val+max(left,right)
        dfs(root)

        return self.max_sum

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

print(root.Max_path_sum(root))
