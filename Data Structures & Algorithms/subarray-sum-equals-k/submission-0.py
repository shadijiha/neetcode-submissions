class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {
            0: 1   # when we find a subarray that matches k, if we remove nothing, then it is res + 1
                    # this is basically here to cover the edge case
        }
        prefix = [0 for _ in nums]

        res = 0
        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = n
            else:
                prefix[i] = prefix[i - 1] + n
            
            curr_prefix = prefix[i]
            diff = curr_prefix - k
            if diff in prefix_count:
                res += prefix_count[diff]

            if curr_prefix in prefix_count:
                prefix_count[curr_prefix] += 1
            else:
                prefix_count[curr_prefix] = 1

        return res