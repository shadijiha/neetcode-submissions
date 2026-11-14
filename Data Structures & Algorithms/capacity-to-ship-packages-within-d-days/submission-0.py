class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        while l <= r:
            m = ((r - l) // 2) + l

            total_days = 1
            load = 0
            for w in weights:
                if load + w > m:
                    total_days += 1
                    load = w
                else:
                    load += w

            if total_days > days:
                l = m + 1
            else:
                r = m - 1
        return l