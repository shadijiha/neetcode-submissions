class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(heights) - 1
        while l < r:
            base = r - l
            h1 = heights[l]
            h2 = heights[r]

            h = min(h1, h2)

            area = base * h
            maxArea = max(maxArea, area)

            if h1 > h2:
                r -= 1
            else:
                l += 1
        
        return maxArea