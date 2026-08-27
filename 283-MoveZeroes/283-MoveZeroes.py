# Last updated: 8/27/2026, 9:34:33 AM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        inter = []
4        for val in nums1:
5            if val in nums2:
6                inter.append(val)
7        unique = list(set(inter))
8        return unique