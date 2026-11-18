class Solution:
    def decodeString(self, s: str) -> str:
        s = f"1[{s}]"

        def dfs(ptr) -> (int, str):
            digit = ""
            while s[ptr].isdigit():
                digit += s[ptr]
                ptr += 1
            
            ptr += 1
            result = ""
            while s[ptr] != "]":
                if s[ptr].isdigit():
                    new_ptr, res_str = dfs(ptr)
                    ptr = new_ptr
                    result += res_str
                else:
                    result += s[ptr]
                ptr += 1
            return ptr, result * int(digit)

        ptr, result = dfs(0)
        return result