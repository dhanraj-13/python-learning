# Last updated: 8/24/2026, 4:12:46 PM
1
2class Solution(object):
3    def isSameTree(self, p, q):
4        if not p and not q:
5            return True
6        if not p or not q:
7            return False
8        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)