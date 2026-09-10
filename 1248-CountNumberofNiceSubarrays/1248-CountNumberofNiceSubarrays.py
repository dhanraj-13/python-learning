# Last updated: 9/10/2026, 1:58:24 PM
1class Solution:
2    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        
5        odds = [-1] + [i for i, num in enumerate(nums) if num % 2 != 0] + [n]
6        
7        total_subarrays = 0
8        
9        for i in range(1, len(odds) - k):
10            left_choices = odds[i] - odds[i - 1]
11            right_choices = odds[i + k] - odds[i + k - 1]
12            
13            total_subarrays += left_choices * right_choices
14            
15        return total_subarrays