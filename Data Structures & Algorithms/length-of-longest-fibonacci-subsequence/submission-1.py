class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        #
        #   [2,3,5,8,13]
        # 2
        # 3
        # 5
        #  
        if len(arr) < 3:
            return 0

        index_map = {x: i for i, x in enumerate(arr)}

        N = len(arr)
        dp = [ [2] * N for _ in range(N)]
        longest = 0

        for i in range(N):
            for j in range(i):
                # we want arr[i] = arr[j] + arr[k]
                arr_k = arr[i] - arr[j]

                if arr_k not in index_map: continue

                k = index_map[arr_k]

                if k < j:
                    dp[j][i] = dp[k][j] + 1
                    longest = max(longest, dp[j][i])

        return longest

