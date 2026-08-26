# Last updated: 8/26/2026, 10:56:08 PM
1class Solution(object):
2    def thirdMax(self, nums):
3        s=sorted(list(set(nums)),reverse=True)
4        if len(s)<3:
5            return max(s)
6        return s[2]