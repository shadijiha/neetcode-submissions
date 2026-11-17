class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        sums = [0] * k

        nums.sort(reverse=True)

        def backtrack(start):
            if start >= len(nums):
                return all(x == sums[0] for x in sums) and all(x > 0 for x in sums)

            for i in range(k):
                if nums[start] + sums[i] > target:
                    continue
                
                sums[i] += nums[start]
                if backtrack(start + 1):
                    return True
                sums[i] -= nums[start]

                if sums[i] == 0:
                    break
            return False
        
        return backtrack(0)
