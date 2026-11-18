class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        nums_map = defaultdict(list)

        for i in range(0, 10):
            nums_map[str(i)].append(str((i - 1) % 10))
            nums_map[str(i)].append(str((i + 1)% 10))

        dead = set(deadends)

        q = deque([("0000", 0)])
        visited = set()

        while q:
            state, moves = q.popleft()

            if state == target:
                return moves

            if state in dead:
                continue
                
            if state in visited:
                continue
            visited.add(state)

            for i in range(len(state)):
                char_state = state[i]
                for next_char_state in nums_map[char_state]:
                    new_state = state[:i] + next_char_state + state[i+1:]
                    q.append((new_state, moves + 1))      
        return -1
