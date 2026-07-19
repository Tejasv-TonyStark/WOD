class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def Preorder(root):
        if root is None:
            return
        ans = []

        def dfs(node,ans):
            if node is None:
                return
            
            ans.append(node.val)
            dfs(node.left,ans)
            dfs(node.right,ans)
        
        dfs(root,ans)
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(TreeNode.Preorder(root))
        
