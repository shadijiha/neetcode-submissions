class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hashS = collections.defaultdict(int)
        hashT = collections.defaultdict(int)

        for c in s:
            hashS[c] += 1
        for c in t:
            hashT[c] += 1
        
        for key in hashS:
            if key not in hashT:
                return False
            
            if hashT[key] != hashS[key]:
                return False
        
        return True
