# Last updated: 8/24/2026, 3:52:50 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        for row in range(0,9,3):
4            for col in range(0,9,3):
5                m=set()
6                for i in range(row,row+3):
7                    for j in range(col,col+3):
8                        if board[i][j]=='.':
9                            continue
10                        if board[i][j] in m:
11                            return False
12                        m.add(board[i][j])
13        for i in range(0,9):
14            m=set()
15            for j in range(0,9):
16                if board[i][j]=='.':
17                    continue
18                if board[i][j] in m:
19                    return False
20                m.add(board[i][j])
21        for i in range(0,9):
22            m=set()
23            for j in range(0,9):
24                if board[j][i]=='.':
25                    continue
26                if board[j][i] in m:
27                    return False
28                m.add(board[j][i])
29        return True
30    
31