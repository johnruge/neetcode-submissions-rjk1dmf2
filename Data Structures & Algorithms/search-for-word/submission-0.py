class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, p, visited):
            if p >= len(word) or (p == len(word) - 1 and board[i][j] == word[p]):
                return True

            moves = valid_moves(i, j, visited)
            for j, k in moves:
                if  p + 1 < len(word) and board[j][k] == word[p + 1]:
                    
                    # include
                    visited.add((j, k))
                    if dfs(j, k, p + 1, visited):
                        return True
 
                    # not include
                    visited.remove((j, k))

            return False
        
        def valid_moves(i, j, visited):
            candidates = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            res = []
            for j, k in candidates:
                if (j, k) not in visited:
                    if (j >= 0 and j < len(board)) and (k >= 0 and k < len(board[0])):
                        res.append((j, k))
            return res
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if dfs(i, j, 0, visited): 
                        return True
        return False 
# let L be the len of the word
# time: m * n * 4^L (but we can say 3^L because the visited set prevents from goinmg directly backwards)
# space: L (this is the recursion stack and visted set)     