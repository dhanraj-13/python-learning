# Last updated: 9/22/2026, 2:47:35 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        max_area = 0
5
6        heights.append(0)
7
8        for i in range(len(heights)):
9            while stack and heights[stack[-1]] > heights[i]:
10                h = heights[stack.pop()]
11
12                if stack:
13                    w = i - stack[-1] - 1
14                else:
15                    w = i
16
17                max_area = max(max_area, h * w)
18
19            stack.append(i)
20
21        return max_area