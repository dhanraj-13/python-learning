# Last updated: 9/18/2026, 12:41:15 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        strs_table = {}
4
5        for string in strs:
6            sorted_string = ''.join(sorted(string))
7
8            if sorted_string not in strs_table:
9                strs_table[sorted_string] = []
10
11            strs_table[sorted_string].append(string)
12
13        return list(strs_table.values())