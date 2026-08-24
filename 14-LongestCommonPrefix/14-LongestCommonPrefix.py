# Last updated: 8/24/2026, 3:51:51 PM
1class Solution(object):
2    def searchInsert(self, nums, target):
3        l = 0
4        r = len(nums) - 1
5        while l <= r:
6            mid = (l + r) // 2
7            if nums[mid] < target:
8                l = mid + 1
9            elif nums[mid] > target:
10                r = mid - 1
11            else:
12                return mid
13        return l
14        