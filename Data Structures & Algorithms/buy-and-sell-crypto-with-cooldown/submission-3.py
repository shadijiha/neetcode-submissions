class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [1,3,4,0,4]
        #
        #                              *
        #                       -1
        #                  2        3
        #            2                  -1
        #       6
        memo = {}
        def dfs(day, holding) -> int:
            if day >= len(prices):
                return 0

            cache_key = (day, holding)
            if cache_key in memo:
                return memo[cache_key]
            
            if not holding:
                skip = dfs(day + 1, holding)
                buy = dfs(day + 1, True) - prices[day]
                
                memo[cache_key] = max(skip, buy)
            else:
                sell = dfs(day + 2, False) + prices[day]
                skip = dfs(day + 1, holding)

                memo[cache_key] = max(skip, sell)
    
            return memo[cache_key]
        return dfs(0, False)