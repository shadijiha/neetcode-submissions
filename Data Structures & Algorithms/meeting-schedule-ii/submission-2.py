"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # We want the maxmimum overlapping intervals at any given moment

        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda interval: interval.start)

        # Ongoing meetings ends
        rooms = []

        for internval in intervals:
            start, end = internval.start, internval.end

            if rooms and rooms[0] <= start: # heap is end time of previous meeting
                # This means that meeting in heap has ended
                heapq.heappop(rooms)
            
            # Assign a room to the meeting
            heapq.heappush(rooms, end)

        return len(rooms)

        
    

