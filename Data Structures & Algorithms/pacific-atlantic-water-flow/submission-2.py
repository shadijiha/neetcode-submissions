class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        resPacific = set()
        resAtlantic = set()

        def dfs(ocean, r, c, prevVal=None):
            if heights[r][c] < prevVal:
                return

            if ocean == "pacific" and (r, c) in resPacific: return 
            elif (r, c) in resAtlantic: return

            if ocean == "pacific":
                resPacific.add((r, c))
            else:
                resAtlantic.add((r, c))

            directions = [
                (0, 1), (0, -1), (1, 0), (-1, 0)
            ]
            for dx, dy in directions:
                rNext, cNext = r + dx, c + dy
                if rNext in range(len(heights)) and cNext in range(len(heights[r])):
                    dfs(ocean, rNext, cNext, heights[r][c])

        
        
        # Pacific
        for r in range(len(heights)):
            dfs("pacific", r, 0, -math.inf)
        for c in range(len(heights[0])):
            dfs("pacific", 0, c, -math.inf)
        
        # Atlantic
        for r in range(len(heights)):
            dfs("atlantic", r, len(heights[r]) - 1, -math.inf)
        for c in range(len(heights[-1])):
            dfs("atlantic", len(heights) - 1, c, -math.inf)
        
        res = resPacific.intersection(resAtlantic)
        return list(res)