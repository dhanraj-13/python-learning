# Last updated: 8/8/2026, 3:20:06 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        num = str(x)
4        if num == num[::-1]:
5            return True
6        else:
7            return False