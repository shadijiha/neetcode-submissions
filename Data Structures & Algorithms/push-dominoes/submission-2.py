class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        q = deque()

        for i, d in enumerate(dominoes):
            if d == "L" or d == "R":
                q.append(i)
        
        while q:
            q_len = len(q)

            # I know this doesn't 100% work because
            # I also need to track who modified the index L or R?
            modified_indicies = set()

            for _ in range(q_len):
                domino_index = q.popleft()
                current = dominoes[domino_index]

                # if R domino_index + 1
                next_index, prev_index = domino_index + 1, domino_index - 1

                if current == "R" and next_index < len(dominoes):
                    if next_index in modified_indicies:
                        dominoes[next_index] = "."
                        
                    elif dominoes[next_index] == ".":
                        dominoes[next_index] = "R"
                        q.append(next_index)
                        modified_indicies.add(next_index)
                elif current == "L" and prev_index >= 0:
                    if prev_index in modified_indicies:
                        dominoes[prev_index] = "."
                        
                    elif dominoes[prev_index] == ".":
                        dominoes[prev_index] = "L"
                        q.append(prev_index)
                        modified_indicies.add(prev_index)

        return "".join(dominoes)
