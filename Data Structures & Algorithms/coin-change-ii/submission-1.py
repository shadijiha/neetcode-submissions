class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Brut force with memo
        # amount = 4, coins = [1,2,3]
        #                               *
        #                       3
        #                   2      1    0
        #               1           0
        #           0
        memo = {}
        def backtrack(i, target_amount):
            if target_amount == 0:
                return 1
            if target_amount < 0:
                return 0
            if (i, target_amount) in memo:
                return memo[(i, target_amount)]

            total_ways = 0
            for j in range(i, len(coins)):
                c = coins[j]
                new_target = target_amount - c
                if new_target >= 0:
                    total_ways += backtrack(j, new_target)

            memo[(i, target_amount)] = total_ways
            return total_ways

        return backtrack(0, amount)