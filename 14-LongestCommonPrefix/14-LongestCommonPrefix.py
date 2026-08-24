# Last updated: 8/24/2026, 3:48:01 PM
1class Solution:
2    def longestCommonPrefix(self, strs):
3        strs.sort()
4        s = ""
5        i = 0
6        length = len(strs)
7
8        while i < len(strs[0]):
9            if strs[0][i] == strs[length - 1][i]:
10                s += strs[0][i]
11            else:
12                break
13            i += 1
14
15        return s