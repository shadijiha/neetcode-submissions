class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)        

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in list(self.pts_count.keys()):
            # is this a diagonal?
            if (abs(py - y) != abs(px - x)) or px == x or py == y:
                continue

            # Do we have matching points
            res += self.pts_count[(x, py)] * self.pts_count[(px, y)] * self.pts_count[(x, y)]
        return res
            
        
