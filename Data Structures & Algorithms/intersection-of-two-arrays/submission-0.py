class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sett = set(nums1) if len(nums1) < len(nums2) else set(nums2)

        
        res = set()

        arr_to_iterate = nums2 if len(nums1) < len(nums2) else nums1
        for n in arr_to_iterate:
            if n in sett and n not in res:
                res.add(n) 
        
        return list(res)