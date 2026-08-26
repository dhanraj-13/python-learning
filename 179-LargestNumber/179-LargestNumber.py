# Last updated: 8/26/2026, 11:29:19 PM
1class Solution:
2    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
3        words1 = {word: idx for idx, word in enumerate(list1)}
4
5        min_sum = math.inf
6        for idx2, word2 in enumerate(list2):
7            if word2 in words1:
8                if words1[word2] + idx2 < min_sum:
9                    min_sum = words1[word2] + idx2
10                    min_words = [word2]
11                elif words1[word2] + idx2 == min_sum:
12                    min_words.append(word2)
13                   
14        return min_words