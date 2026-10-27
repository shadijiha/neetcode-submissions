class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # because internvals are already sorted, then the problem is easier
        # https://www.youtube.com/watch?v=A8NUOmlwOlM
        res = []

        for i in range(len(intervals)):
            # if not overlapping with current and smaller than current
            # we add it and return because it means no future overlap will occur
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return [*res, *intervals[i:]]
            # otherwise it is not the right place to insert it
            # continue inserting lesser intervals
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # it is right place but it overlaps with other intervals
                # update it and do not insert it, in supsequent loops, the first if statement
                # will insert it when it is the correct time OR it will be inserted before we return below
                newInterval = [
                    min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])
                ]

        # this means the new interval is larger than all other intervals
        # OR was merged with other intervals and its Right is larger than all other intervals
        res.append(newInterval)

        return res