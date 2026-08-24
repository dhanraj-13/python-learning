# Last updated: 8/24/2026, 4:16:45 PM
1# Definition for a  binary tree node
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    # @param num, a list of integers
10    # @return a tree node
11    # 12:37
12    def sortedArrayToBST(self, num):
13        if not num:
14            return None
15
16        mid = len(num) // 2
17
18        root = TreeNode(num[mid])
19        root.left = self.sortedArrayToBST(num[:mid])
20        root.right = self.sortedArrayToBST(num[mid+1:])
21
22        return root