# Last updated: 9/18/2026, 12:02:38 PM
1class Solution:
2    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
3        self.ans = ""
4        self.dfs(root, "")
5        return self.ans
6
7    def dfs(self, root, current_string):
8        # If the current node is none, return
9        if not root:
10            return
11
12      
13        current_string = chr(root.val + ord('a')) + current_string
14
15        if not root.left and not root.right:
16           
17            if not self.ans or self.ans > current_string:
18                self.ans = current_string
19        
20        self.dfs(root.left, current_string)
21        self.dfs(root.right, current_string)