class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        sides = [0] * 4
        target = sum(matchsticks) // 4

        matchsticks = sorted(matchsticks, reverse=True)

        def backtrack(start):
            if start >= len(matchsticks):
                return all(x == target for x in sides)

            for i in range(4):
                if sides[i] + matchsticks[start] > target:
                    continue
                sides[i] += matchsticks[start]
                if backtrack(start + 1):
                    return True
                sides[i] -= matchsticks[start]
            
            return False

        return backtrack(0)