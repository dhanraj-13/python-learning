# Last updated: 9/18/2026, 12:28:56 PM
1class Solution:
2    def isPossible(self, nums: List[int]) -> bool:
3        subsequences = []
4        
5        for num in nums:
6            while subsequences and subsequences[0][0] + 1 < num:
7                sub = heapq.heappop(subsequences)
8                if sub[1] < 3:
9                    return False
10            
11            if not subsequences or subsequences[0][0] == num:
12                heapq.heappush(subsequences, [num, 1])
13            else:
14                sub = heapq.heappop(subsequences)
15                sub[0] += 1
16                sub[1] += 1
17                heapq.heappush(subsequences, sub)
18                
19        while subsequences:
20            sub = heapq.heappop(subsequences)
21            if sub[1] < 3:
22                return False
23            
24        return True