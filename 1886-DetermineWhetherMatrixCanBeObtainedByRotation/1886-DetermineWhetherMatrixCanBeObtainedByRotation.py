# Last updated: 9/25/2026, 5:41:30 PM
1class Solution:
2    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
3        for _ in range(4):
4            if mat == target:
5                return True
6
7            mat = [list(row) for row in zip(*mat[::-1])]
8        return False