class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # https://www.youtube.com/watch?v=zx5Sw9130L0

        max_area = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, larger_height = stack.pop()
                area = (i - index) * larger_height
                max_area = max(max_area, area)

                start = index
            
            stack.append((start, h))

        # Remain elements can be extended the entire length of the histogram
        histo_length = len(heights)
        for i, h in stack:
            area = (histo_length - i) * h
            max_area = max(max_area, area)

        return max_area