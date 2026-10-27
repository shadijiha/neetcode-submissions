"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        # is intervals sorted?
        intervals.sort(key=lambda interval: interval.start)

        prev = intervals[0]

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start < prev.end:
                return False
            prev = interval
        
        return True


