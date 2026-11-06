class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        #                 ^
        #
        #q=[38, 36, 35]   > 40
        #q=[1, 3, 4]
        # result[0]  = 1  
        # result[2] =  1  
        # result[4] = 5 - 4
        # result[3] = 5- 3
        # result[1] = 5 - 1
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > temperatures[stack[-1]]:
                top_index = stack.pop()
                result[top_index] = i - top_index
            
            stack.append(i)

        return result
