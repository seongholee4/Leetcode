# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0
    
    def root_to_tree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        tree = TreeNode(root[0])
        queue = [tree]
        i = 1
        while queue and i < len(root):
            node = queue.pop(0)
            if i < len(root) and root[i] is not None:
                node.left = TreeNode(root[i])
                queue.append(node.left)
            i+=1

            if i < len(root) and root[i] is not None:
                node.right = TreeNode(root[i])
                queue.append(node.right)
            i+=1
        
        return tree
    
    def print_tree(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return
        
        queue = [(root, 0)]
        current_level = 0

        while queue:
            node, level = queue.pop(0)
            
            if level != current_level:
                print()  # Move to the next line for the next level
                current_level = level


            # print(node.val, end=" ")
            # if node.left:
            #     queue.append((node.left, level + 1))
            # if node.right:
            #     queue.append((node.right, level + 1))
            if node:
                print(node.val, end=" ")
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            else:
                print("None", end=" ")




s = Solution()
root = [3,9,20,None,None,15,7]
tree = s.root_to_tree(root)
# print(tree.val, tree.left.val)
s.print_tree(tree)

