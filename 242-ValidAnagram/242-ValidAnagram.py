# Last updated: 7/14/2026, 1:57:26 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)