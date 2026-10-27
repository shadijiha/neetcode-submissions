class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [1,2,3,4]
        # [2,2,4,1]
        #  ^
        # [-1,0,-1,3]
        if len(gas) != len(cost):
            raise Exception("Cost and gas array length must be equal")

        if sum(gas) < sum(cost):
            return -1
        
        totalGasOverflow = 0
        startPosition = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i] 
            totalGasOverflow += diff

            if totalGasOverflow < 0:
                totalGasOverflow = 0
                startPosition = i + 1
                continue

        return startPosition
        