class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=lXVy6YWFcRM
        #
        # 3 cases
        # - all positive: maxProduct
        # - array contains negative: minProduct and maxProduct so we can * 
        # - array has 0 we want to rest to 1, 1
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            preModifcationMax = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * preModifcationMax, n * curMin, n)
            res = max(res, curMax, curMin)

        return res

        