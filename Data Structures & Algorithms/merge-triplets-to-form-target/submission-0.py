class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filtered_triplets = []
        x, y, z = target

        for triplet in triplets:
            a, b, c = triplet

            if a > x or b > y or c > z:
                continue
            filtered_triplets.append(triplet)
        
        # If empty
        if not filtered_triplets:
            return False
        
        # loop and check if any contains target
        contains_x = contains_y = contains_z = False

        for good_triplet in filtered_triplets:
            a, b, c = good_triplet
            contains_x = contains_x or a == x
            contains_y = contains_y or b == y
            contains_z = contains_z or c == z
        
        return contains_x and contains_y and contains_z
