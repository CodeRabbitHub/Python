from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        # lets sort the tickets 'source-destination' in a way that
        # 'destination' pops up in Lexical order
        tickets.sort(key=lambda x: x[1], reverse=True)

        # creating graph {source:[destinations]}
        flightMap = defaultdict(list)

        # populating the graph
        for source, destination in tickets:
            flightMap[source].append(destination)

        result = []
        stack = [("JFK")]

        # Start with JFK as starting and keep adding the next airport to traverse to
        # the top of the stack. If we cannot travel further from an airport then
        # remove it from stack and append to result. This airport should be visited last.
        # This is why we reverse the result After this backtrack to the top airport in
        # stack and continue to traverse

        while stack:
            curr = stack[-1]

            # check if curr in graph as there may be a case wherer there is no out edge
            # from an airport, In that case it wont be present as key in graph
            if curr in flightMap and flightMap[curr]:
                stack.append(flightMap[curr].pop())

            else:
                # If there is no further children to traverse then add it to result.
                result.append(stack.pop())

        return result[::-1]
