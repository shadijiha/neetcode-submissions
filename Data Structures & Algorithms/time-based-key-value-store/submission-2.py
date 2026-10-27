
class TimeMap:

    def __init__(self):
        self.keys = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamps of set are strictly increasing.
        if key in self.keys:
            self.keys[key].append((timestamp, value))
            return

        self.keys[key] = [(timestamp, value)]
        

    def get(self, key: str, target: int) -> str:
        if key not in self.keys or not self.keys[key]:
            return ""
        
        candidate = ""
        l, r = 0, len(self.keys[key]) - 1
        while l <= r:
            m = ((r - l) // 2) + l

            t, v = self.keys[key][m]

            if t == target:
                return v
            elif target > t:
                candidate = v
                l = m + 1
            else:
                r = m - 1
        return candidate
                


        
