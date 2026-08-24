# Last updated: 8/24/2026, 3:47:20 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3    
4        # rti is a dict for roman to intgers values
5        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
6
7        # ans is for our sum value
8        ans=0
9
10        # for loop till len(s)-1 cause for last Roman Value we cant compare
11        for i in range(len(s)-1):
12            if rti[s[i]] < rti[s[i+1]]:
13                ans = ans - rti[s[i]]
14            else:   
15                ans = ans + rti[s[i]]
16
17        # So we add the last value and return the final ans
18        return ans+rti[s[-1]]