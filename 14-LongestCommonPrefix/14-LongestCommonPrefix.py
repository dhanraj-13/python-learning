# Last updated: 8/24/2026, 3:51:22 PM
1class Solution:
2    def removeDuplicates(self, nums):
3
4        if len(nums) == 0:
5            return 0
6
7        k = 1
8
9        for i in range(1, len(nums)):
10
11            if nums[i] != nums[i-1]:
12                nums[k] = nums[i]
13                k += 1
14
15        return k