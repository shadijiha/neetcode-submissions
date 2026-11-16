class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
            

        l, r = 1, max(quantities)
        while l <= r:
            m = ((r - l) // 2) + l

            stores_needed = 0
            for q in quantities:
                stores_needed += math.ceil(q / m)
            
            if stores_needed > n:
                l = m + 1
            else:
                r = m - 1

        return l 


