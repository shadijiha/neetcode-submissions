class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        cur_max = arr[-1]
        arr[-1] = -1

        for i in reversed(range(len(arr) - 1)):
            tmp = arr[i]
            arr[i] = cur_max
            cur_max = max(cur_max, tmp)

        return arr