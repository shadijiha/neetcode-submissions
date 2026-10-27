class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #
        #   [1,4,2,2,3,5,3,4]
        # 
        # {1: 1, 2:2, 3:2, 4:2, 5: 1}
        if len(hand) % groupSize != 0:
            return False
        
        frequencyMap = collections.Counter(hand)
        groupCount = len(hand) // groupSize
        
        for i in range(groupCount):
            cardToSearch = min(frequencyMap)
            
            for j in range(groupSize):
                if cardToSearch not in frequencyMap or frequencyMap[cardToSearch] <= 0:
                    return False
                frequencyMap[cardToSearch] -= 1
                if frequencyMap[cardToSearch] <= 0:
                    del frequencyMap[cardToSearch]

                cardToSearch += 1
        return True


        