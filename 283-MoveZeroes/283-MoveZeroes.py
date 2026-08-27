# Last updated: 8/27/2026, 9:15:56 AM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        for i in range(len(nums)):
4            if nums[i] == 0:
5                for j in range(i+1, len(nums)):
6                    if nums[j] != 0:
7                        nums[i], nums[j] = nums[j], nums[i]
8                        break