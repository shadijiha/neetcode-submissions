class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in cache:
                length = 1
                currNum = n + 1
                while currNum in cache:
                    currNum += 1
                    length += 1
                
                longest = max(longest, length)
        
        return longest
