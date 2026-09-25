# Last updated: 9/25/2026, 9:46:30 AM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        if dividend ==0:
4            return 0
5
6        neg=(dividend<0) != (divisor<0)
7        dividend = abs(dividend)
8        divisor = abs(divisor)
9        result = 0
10
11        while dividend >= divisor:
12            temp = divisor
13            multiple = 1
14            
15            while dividend >= temp + temp:
16                temp += temp
17                multiple += multiple
18
19            dividend -= temp
20            result += multiple
21
22        if neg:
23            result = -result
24                    
25        if result > 2**31 -1:
26            result = 2**31 -1
27
28        if result < -2**31:
29            result = -2**31
30                    
31        return result