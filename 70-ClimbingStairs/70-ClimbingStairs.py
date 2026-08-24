# Last updated: 8/24/2026, 4:08:54 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        cache = {}
4        
5        def rec_f(n):
6            # 1. Return cached result if already computed
7            if n in cache:
8                return cache[n]
9            # 2. Base cases: n <= 2 instead of n < 2 (n=1 -> 1 way, n=2 -> 2 ways)
10            elif n <= 2:
11                result = n
12            # 3. Fibonacci recurrence: f(n) = f(n-1) + f(n-2)
13            else:
14                result = rec_f(n - 1) + rec_f(n - 2)
15            
16            # Save to cache before returning
17            cache[n] = result
18            return result
19        
20        return rec_f(n)