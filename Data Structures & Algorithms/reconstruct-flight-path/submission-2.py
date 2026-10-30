class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        for fromm, to in sorted(tickets, reverse=True):
            graph[fromm].append(to)

        stack = ["JFK"]
        result = []

        while stack:
            while graph[stack[-1]]:
                nextt = graph[stack[-1]].pop()
                stack.append(nextt)
            result.append(stack.pop())

        return list(reversed(result))