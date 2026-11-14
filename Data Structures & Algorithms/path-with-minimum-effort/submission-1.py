class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        N, M = len(heights), len(heights[0])
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        q = [(0, 0, 0)] # effort, i, j
        visited = set()

        while q:
            effort, i, j = heapq.heappop(q)

            if (i, j) in visited:
                continue
            visited.add((i, j))

            if i == N - 1 and j == M - 1:
                return effort

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if x not in range(N) or y not in range(M):
                    continue
                
                heapq.heappush(q, (
                    max(effort, abs(heights[i][j] - heights[x][y])),
                    x, y
                ))
        return 0