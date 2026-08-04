# Last updated: 8/4/2026, 12:40:21 PM
1class Solution:
2    def findReplaceString(self, s: str, inx: List[int], sources: List[str], targets: List[str]) -> str:
3        op =[]
4        for i in range(len(inx)):
5            op.append((inx[i], sources[i],targets[i]))
6        op.sort(reverse=True)
7        for inx, source, target in op:
8            if s[inx:inx +len(source)] == source:
9                s = s[:inx] + target + s[inx + len(source):]
10        return s