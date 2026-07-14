# Last updated: 7/14/2026, 1:57:21 PM
class Solution:
    def reverseString(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1