import heapq


def prim_min_spanning_tree(n, graph):
    """
    graph: {
        node1: [(edge1, weight1), (edge2, weight2), ..., (edgeM, weightM)],
        node2: [(edge1, weight1), (edge2, weight2), ..., (edgeM, weightM)],
        ...
        nodeN: [(edge1, weight1), (edge2, weight2), ..., (edge2M, weight2M)]
    }

    Time and Space Complexity: O(N LOG(N)) where N = total number of (edge, weight) pairs in graph
    """
    start = 0
    cost = 0
    visited = {start}
    min_heap = []
    for node, weight in graph[start]:
        heapq.heappush(min_heap, (weight, node))
    while len(visited) < n:
        weight, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            cost += weight
            for edge_node, weight_edge_node in graph[node]:
                if edge_node not in visited:
                    heapq.heappush(min_heap, (weight_edge_node, edge_node))
    return cost
