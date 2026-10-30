class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # review this https://www.youtube.com/watch?v=5G0HyBhqpQo
        graph = defaultdict(list)
        for fromm, to in sorted(tickets):
            graph[fromm].append(to)

        stack = ["JFK"]
        result = []

        while stack:
            while graph[stack[-1]]:
                nextt = graph[stack[-1]].pop(0)
                stack.append(nextt)
            result.append(stack.pop())

        return list(reversed(result))