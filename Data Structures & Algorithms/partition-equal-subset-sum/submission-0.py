class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
            
        target = total // 2

        sums = set()
        sums.add(0)
        
        for n in nums:
            tempSums = set()
            for s in sums:
                tempSums.add(n + s)
                tempSums.add(s)
            sums = tempSums

        return target in sums

        