class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        #
        # [6,3,1,8]
        # [8,5,2,9]
        # [10,7,3,10]
        pairs = zip(position, speed)

        fleets = []
        for p, s in reversed(sorted(pairs)):
            reach_destination_at = (target - p) / s

            if not fleets or reach_destination_at > fleets[-1]:
                fleets.append(reach_destination_at)
            
        return len(fleets)