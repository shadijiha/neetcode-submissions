class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQueries = sorted((q, i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        intervalLengthHeap = []
        i = 0
        
        for query, indexToInsert in sortedQueries:
            # add intervals with start less than query
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(intervalLengthHeap, (end - start + 1, end))
                i += 1
            
            # remove internvals that have end less than query
            while intervalLengthHeap and intervalLengthHeap[0][1] < query:
                heapq.heappop(intervalLengthHeap)

            if intervalLengthHeap:
                res[indexToInsert] = intervalLengthHeap[0][0]

        return res