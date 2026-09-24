class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def getNeighbors(i:int, j:int) -> List[Tuple[int, int]]:
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            res = []
            for c, k in directions:
                newi, newj = i + c, j + k
                if 0 <= newi < len(grid) and 0<= newj < len(grid[0]) and (newi, newj) not in visited and grid[newi][newj] == 1:
                    res.append((newi, newj))
                    visited.add((newi, newj))
            return res

        def bfs(i, j):
            print(i, j)
            visited.add((i, j))
            q = deque([(i, j)])
            count = 0

            while q:
                count += 1
                curri, currj = q.popleft()
                q.extend(getNeighbors(curri, currj))

            return count
        
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    res = max(res, bfs(i , j)) 

        return res