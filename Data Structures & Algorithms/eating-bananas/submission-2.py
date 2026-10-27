class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #
        #   [1,4,3,2], h = 9  k=1
        #    1
        MIN_K, MAX_K = 1, max(piles)
        
        l, r = MIN_K, MAX_K

        while l <= r:
            k = ((r - l) // 2) + l
            total_hours = 0

            for p in piles:
                total_hours += math.ceil(p / k)
            
            if total_hours > h:
                l = k + 1
            else:
                r = k - 1
 
        return l
        