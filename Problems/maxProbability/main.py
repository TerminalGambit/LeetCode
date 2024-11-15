import heapq

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        # Create graph as an adjacency list
        graph = {i: [] for i in range(n)}
        for ((u, v), prob) in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        # Priority queue: (negative probability for max-heap simulation, node)
        pq = [(-1.0, start)]  # Start with a probability of 1 (use -1 for max-heap)
        # Map to store the maximum probability to reach each node
        max_prob = [0] * n
        max_prob[start] = 1.0

        while pq:
            # Get the node with the current maximum probability
            current_prob, u = heapq.heappop(pq)
            current_prob = -current_prob  # Convert back to positive since we're using negative for max-heap

            # If we reach the end node, return the probability as this is the highest one due to max-heap
            if u == end:
                return current_prob

            # Process each neighbor
            for v, prob in graph[u]:
                new_prob = current_prob * prob
                # Only consider this new path if it's better than any previously found path to v
                if new_prob > max_prob[v]:
                    max_prob[v] = new_prob
                    heapq.heappush(pq, (-new_prob, v))

        # If we exit the loop, it means no path was found
        return 0.0


# Example usage:
sol = Solution()
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
print(sol.maxProbability(n, edges, succProb, start, end))  # Output: 0.25
