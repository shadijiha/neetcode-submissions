class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #
        # ["act","pots","tops","cat","stop","hat"]
        #  ^
        # O(n*L) n=len(strs) and L = total string length
        # buckets = {
        #    (a: 1, c:1, t:1): ["act", "cat"]
        # }
        buckets = collections.defaultdict(list)

        for string in strs:
            frq = collections.Counter(string)
            buckets[tuple(sorted(frq.items()))].append(string)

        return list(buckets.values())
