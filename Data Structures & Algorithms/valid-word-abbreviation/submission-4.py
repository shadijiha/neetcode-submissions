class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif not abbr[j].isdigit():
                return False
            else:
                digit = ""
                while j < len(abbr) and abbr[j].isdigit():
                    digit += abbr[j]
                    j += 1
                
                if len(digit) > 1 and digit[0] == "0":
                    return False
                
                i += int(digit)

        return i == len(word) and j == len(abbr)
            