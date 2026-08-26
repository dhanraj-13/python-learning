# Last updated: 8/26/2026, 10:44:28 PM
1class Solution:
2    def maxProduct(self, words: List[str]) -> int:
3        #Solution2 (Optimal)
4        ans = 0
5        n = len(words)
6        binary_rep = [0]*n
7        for i in range(n):
8            curr_word = words[i]
9            for letter in curr_word:
10                binary_rep[i] = binary_rep[i] | (1<<(ord(letter)-ord('a')))
11            for j in range(i):
12                if binary_rep[i] & binary_rep[j] == 0:
13                    ans = max(ans, len(words[i])*len(words[j]))
14        return ans