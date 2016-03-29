"""Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        return self.helper(root,result)
        
        
    def helper(self,node,result):
        if not node:
            return result
        result.append(node.val)
        self.helper(node.left,result)
        self.helper(node.right,result)
        return result

# beats 38 % of submissions

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop()
            
            result.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            
        
        return result