# Last updated: 9/1/2026, 4:44:02 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        result = 0
4        for num in nums:
5            result = result ^ num
6        return result
7
8        #using xor ^