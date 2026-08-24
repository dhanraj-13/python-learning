# Last updated: 8/24/2026, 3:56:31 PM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        i = len(a) - 1
4        j = len(b) - 1
5        carry = 0
6        reverse_answer = []
7
8        while i >= 0 or j >= 0 or carry:
9            bit_a = int(a[i]) if i >= 0 else 0
10            bit_b = int(b[j]) if j >= 0 else 0
11
12            total = bit_a + bit_b + carry
13            digit = str(total % 2)
14            reverse_answer.append(digit)
15            carry = total // 2
16
17            i -= 1
18            j -= 1
19
20        return ''.join(reversed(reverse_answer))