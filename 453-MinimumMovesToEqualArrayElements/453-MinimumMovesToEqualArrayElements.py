# Last updated: 7/14/2026, 1:57:20 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)

        moves = 0

        for i in nums:
            moves += i - minimum

        return moves