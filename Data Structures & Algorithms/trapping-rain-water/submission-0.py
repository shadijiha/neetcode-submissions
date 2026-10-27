class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = [0 for _ in height]
        maxRight = [0 for _ in height]

        for i in range(len(height)):
            if i == 0:
                maxLeft[i] = height[i]
                continue
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        for i in reversed(range(len(height))):
            if i == len(height) - 1:
                maxRight[i] = height[i]
                continue
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        result = [0 for _ in height]
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water < 0:
                water = 0
            result[i] = water

        return sum(result)
        