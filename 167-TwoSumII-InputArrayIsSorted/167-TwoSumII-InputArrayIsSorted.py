# Last updated: 8/5/2026, 2:36:26 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left = 0
4        right = len(numbers)-1
5        while left < right:
6            total = numbers[left] + numbers[right]
7            if total == target:
8                return [left+1 ,right+1]
9            elif total < target:
10                left +=1
11            else:
12                right -=1