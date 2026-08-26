# Last updated: 8/26/2026, 11:00:00 PM
1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        g.sort()
4        s.sort()
5        count = 0
6        i = 0
7        j = 0
8        while i < len(g) and j< len(s):
9            if s[j] >= g[i]:
10                count+=1
11                i+=1 
12            j+=1
13        return count
14        