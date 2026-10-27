class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        resPacific = set()
        resAtlantic = set()

        def dfs(r, c, container: Set[Tuple[int, int]]):
            if (r, c) in container:
                return

            container.add((r, c))
            directions = [
                (0, 1), (0, -1), (1, 0), (-1, 0)
            ]
            for dx, dy in directions:
                rNext, cNext = r + dx, c + dy
                if rNext in range(len(heights)) and cNext in range(len(heights[r])) \
                    and heights[rNext][cNext] >= heights[r][c]:
                    dfs(rNext, cNext, container)

        
        # Pacific
        for r in range(len(heights)):
            dfs(r, 0, resPacific)
        for c in range(len(heights[0])):
            dfs(0, c, resPacific)
        
        # Atlantic
        for r in range(len(heights)):
            dfs(r, len(heights[r]) - 1, resAtlantic)
        for c in range(len(heights[-1])):
            dfs(len(heights) - 1, c, resAtlantic)
        
        res = resPacific.intersection(resAtlantic)
        return list(res)

        