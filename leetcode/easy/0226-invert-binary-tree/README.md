# Invert Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree, invert the tree, and return  *its root*.

 

 **Example 1:** 

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```

 **Example 2:** 

```
Input: root = [2,1,3]
Output: [2,3,1]

```

 **Example 3:** 

```
Input: root = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.5 MB (beats 20.35%)  
**Submitted:** 2026-07-10T06:54:56.929Z  

```py
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node):
            if node:
                swap(node.left)
                swap(node.right)
                node.left,node.right=node.right,node.left
        swap(root)
        return(root)
```

---

[View on LeetCode](https://leetcode.com/problems/invert-binary-tree/)