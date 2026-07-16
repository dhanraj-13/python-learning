# Last updated: 7/16/2026, 4:17:21 PM
1import random
2
3class Solution:
4
5    def __init__(self, nums):
6        self.original = nums[:]
7
8    def reset(self):
9        return self.original
10
11    def shuffle(self):
12        arr = self.original[:]
13        random.shuffle(arr)
14        return arr