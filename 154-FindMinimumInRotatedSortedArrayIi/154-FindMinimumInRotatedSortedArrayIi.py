# Last updated: 7/14/2026, 1:57:28 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        for i in nums:
            if i < minimum:
                minimum = i

        return minimum
        