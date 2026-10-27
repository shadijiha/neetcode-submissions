class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # nums = [1, 1, 1, 2, 3, 9]  , k=1
        # len(nums) = 6
        # [0, 1,     2,   3, 4, 5, 6]
        #    [2,3,9]     [1]
        bucketSortMap = [[] for _ in range(len(nums) + 1)]
        freqMap = {}

        for num in nums:
            s = str(num)
            if s not in freqMap:
                freqMap[s] = 0
            
            prevFreq = freqMap[s]
            freqMap[s] += 1
            newFreq = prevFreq + 1

            if bucketSortMap[prevFreq]:
                bucketSortMap[prevFreq].remove(num)
            
            if not bucketSortMap[newFreq]:
                bucketSortMap[newFreq] = []
            
            bucketSortMap[newFreq].append(num)
        
        result = []
        for i in range(len(bucketSortMap)):
            reverseIndex = len(bucketSortMap) - i - 1
            curr = bucketSortMap[reverseIndex]
            result.extend(curr)

            if len(result) >= k:
                break
        return result[:k]

        
        
              


        