# Last updated: 8/7/2026, 12:39:31 PM
1class Solution:
2    def circularArrayLoop(self, nums: List[int]) -> bool:
3        n = len(nums)
4
5        def nxt(i):
6            return (i + nums[i]) % n
7
8        for i in range(n):
9
10            sp = i
11            fp = i
12            curr_dir = nums[i] > 0
13
14            while True:
15
16                if (nums[sp] > 0) != curr_dir:
17                    break
18
19                if (nums[fp] > 0) != curr_dir:
20                    break
21
22                if (nums[nxt(fp)] > 0) != curr_dir:
23                    break
24
25                sp = nxt(sp)
26                fp = nxt(nxt(fp))
27
28                if sp == fp:
29
30                    if sp == nxt(sp):
31                        break
32
33                    return True
34
35        return False