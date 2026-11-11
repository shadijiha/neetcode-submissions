class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #
        # we want to seperate the array into 2 subsets such as Sum(A) - Sub(B) = minumum
        # that's only possible of Sum(B) = sum // 2
        # so dp = [False] * len(stones)
        # let dp[i] = can we sum a subset to i
        total = sum(stones)
        half = total // 2

        dp = [False] * (half + 1)
        dp[0] = True

        for stone in stones:
            for i in reversed(range(stone, half + 1)): 
                dp[i] = dp[i] or dp[i - stone]

        print(dp)
        largest_achivable_sum = 0
        for s in reversed(range(len(dp))):
            if dp[s]:
                largest_achivable_sum = s
                break

        return abs( largest_achivable_sum - total + largest_achivable_sum )
        