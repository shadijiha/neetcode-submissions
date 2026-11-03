class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # [1, 2, 7, 99]
        # [4, 5, 43]
        # 
        # [1, 2, 4, 5, 43, 99]

        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        # left right ptr for A
        l, r = 0, len(A) - 1

        while True:
            i = ((r - l) // 2) + l # A
            j = half - i - 1 - 1  # B

            Aleft = A[i]        if i >= 0           else -math.inf
            Aright = A[i + 1]   if i + 1 < len(A)   else math.inf
            Bleft = B[j]        if j >= 0           else -math.inf
            Bright = B[j + 1]   if j + 1 < len(B)   else math.inf

            if Aleft <= Bright and Bleft <= Aright:
                # left partition is correct
                if total % 2 != 0:
                    # Compute odd len median
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


     

        