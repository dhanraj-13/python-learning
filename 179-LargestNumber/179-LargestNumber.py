# Last updated: 8/26/2026, 11:13:43 PM
1class Solution:
2    def findRelativeRanks(self, scores: List[int]) -> List[str]:
3        heap = []
4        for i, score in enumerate(scores):
5            heapq.heappush(heap, (-score, i))
6
7        ranks = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
8
9        result = [0] * len(scores)
10
11        for rank in range(len(scores)):
12            _, idx = heapq.heappop(heap)
13            result[idx] = ranks.get(rank, str(rank + 1))
14
15
16        return result 