# Last updated: 9/1/2026, 1:46:03 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4        for num in nums:
5            if num in seen:
6                return True
7            else:
8                seen.add(num)
9        return False