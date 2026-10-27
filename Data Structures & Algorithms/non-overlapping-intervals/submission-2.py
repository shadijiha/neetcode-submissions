class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,2],[1,4],[2,4]]
        if len(intervals) <= 1:
            return 0

        intervals.sort()

        res = 0
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
            else:
                prev = [
                    min(prev[0], intervals[i][0]),
                    min(prev[1], intervals[i][1])
                ] 
                res += 1
        return res