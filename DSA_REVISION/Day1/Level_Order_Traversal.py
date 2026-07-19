from collections import deque
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order_traversal(root):

       
        if root is None:
            return []
        queue = deque([root])
        ans = []

        while queue:

            node = queue.popleft()
            

            

            ans.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(TreeNode.level_order_traversal(root))
        
