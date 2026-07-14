# Last updated: 7/14/2026, 1:57:27 PM
class Solution:
    def rotate(self, nums, k):

        n = len(nums)
        k = k % n

        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)