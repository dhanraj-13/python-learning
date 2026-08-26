# Last updated: 8/26/2026, 11:08:25 PM
1rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))
2
3
4
5class Solution:
6    def findWords(self, words: list[str]) -> list[str]:
7        
8        
9        return [w for w in words if any(set(w.lower()).issubset(row) for row in rows)]