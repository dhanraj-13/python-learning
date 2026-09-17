# Last updated: 9/17/2026, 11:47:07 AM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack = [-1]
4        max_len = 0
5
6        for i in range(len(s)):
7            if s[i] == "(":
8                stack.append(i)
9            else:
10                stack.pop()
11                if len(stack) == 0:
12                    stack.append(i)
13                else:
14                    max_len = max(max_len, i - stack[-1])
15        
16        return max_len