class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Key takeaway
        # need to start with the car the closest to target because
        # it will dictate all others
        pairs = zip(position, speed)

        fleets = []
        for p, s in reversed(sorted(pairs)):
            reach_destination_at = (target - p) / s

            # Only add if it will reach the destination with larger time 
            # than the top of the stack (cars in front)
            if not fleets or reach_destination_at > fleets[-1]:
                fleets.append(reach_destination_at)
            
        return len(fleets)