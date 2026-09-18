# Last updated: 9/18/2026, 12:47:00 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        # using radix sort
4        def radixSort(nums):
5            if nums == []:
6                return []
7            radixArray = [[] for i in range(10)]
8            maxValue = max(nums)
9            exp = 1
10            while (maxValue // exp) > 0:
11                while len(nums) != 0:
12                    ln = nums.pop()  # last number
13                    d = (ln // exp) % 10
14                    radixArray[d].append(ln)
15                for arr in radixArray:
16                    while len(arr) != 0:
17                        nums.append(arr.pop())
18                exp = exp * 10
19            return nums
20        left = []
21        right = []
22        for i in nums:
23            if i < 0:
24                left.append(-1*i)
25            else:
26                right.append(i)
27        left = radixSort(left)
28        right = radixSort(right)
29        neg = [-1*i for i in left[::-1]]
30        return neg + right