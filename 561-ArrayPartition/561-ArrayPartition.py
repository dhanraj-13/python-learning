# Last updated: 7/14/2026, 1:57:16 PM
class Solution:
   def arrayPairSum (self,nums):
    nums.sort()
    a = 0
    for i in range (0, len(nums), 2):
        a += nums[i]

    return a