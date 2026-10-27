class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # Sort internvals
        intervals.sort()

        res = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > prev[1]:
                res.append(prev)
                prev = intervals[i]
            else:
                merged = [
                    min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])
                ]
                prev = merged

        res.append(prev)
        return res