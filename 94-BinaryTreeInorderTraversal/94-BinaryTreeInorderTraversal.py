# Last updated: 8/24/2026, 4:17:46 PM
1class Solution:
2    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
3        st = []
4        res = []
5
6        while root or st:
7            while root:
8                st.append(root)
9                root = root.left
10            
11            root = st.pop()
12            res.append(root.val)
13
14            root = root.right
15        
16        return res   