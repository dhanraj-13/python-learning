# Last updated: 9/1/2026, 3:58:25 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        seen = set()
4        for num in nums:
5            if num in seen:
6                return num
7            seen.add(num)