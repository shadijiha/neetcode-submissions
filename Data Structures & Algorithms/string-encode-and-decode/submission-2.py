class Solution:

    def encode(self, strs: List[str]) -> str:
        # "5@llo","World"
        # 5@5@llo5@World
        strBuilder = [None] * len(strs)

        for i, string in enumerate(strs):
            strBuilder[i] = f"{len(string)}@{string}"

        return "".join(strBuilder)

    def decode(self, s: str) -> List[str]:
        charsRead = 0
        result = []

        while charsRead < len(s):
            # Read the length
            encodedLength = ""
            while s[charsRead].isdigit():
                encodedLength += s[charsRead]
                charsRead += 1
            encodedLength = int(encodedLength)

            # Skip the delimiter
            charsRead += 1

            strBuilder = [None] * encodedLength
            count = 0
            while count < encodedLength:
                strBuilder[count] = s[charsRead]
                count += 1
                charsRead += 1

            result.append("".join(strBuilder))
        return result
            
