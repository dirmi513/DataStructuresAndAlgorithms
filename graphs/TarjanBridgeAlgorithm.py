# Leetcode questions that utilize this algorithm:
# 1) https://leetcode.com/problems/critical-connections-in-a-network/submissions/
from collections import defaultdict


def tarjan_bridge_algorithm(n, edges):
    """Returns a list of edges from a graph that are
    "critical connections", i.e. if you remove this edge,
    the graph will disconnect.

    Args:
          n - number of nodes
          edges - a list of edges from node u to v
    """
    graph = create_undirected_graph(edges)
    # only want to visit each node once
    visited = [False for _ in range(n)]
    # keep track of the id/discovery time of each node, AND
    # the minimum node (based on discovery time) that you can reach the current node from
    id_min = defaultdict(dict)
    # to assign ids and initial mins
    counter = 0
    answer = []
    dfs(0, -1, answer, graph, visited, id_min, counter)
    return answer


def create_undirected_graph(edges):
    """Given an array of UNDIRECTED edges
    [[u, v], [u1, v1], ..., [uN, vN]], convert this
    to a graph data structure using a dictionary.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[v].append(u)
        graph[u].append(v)
    return graph


def dfs(node, parent, critical_edges, graph, visited, id_min, counter):
    if visited[node]:
        return
    visited[node] = True
    id_min[node]["id"] = counter
    id_min[node]["min"] = counter
    counter += 1
    for node2 in graph[node]:
        if node2 == parent:
            continue
        dfs(node2, node, critical_edges, graph, visited, id_min, counter)
        # If the id ("discovery time") of the current node is less than
        # the min node that node2 can be reached from, then there is no other way
        # to get to node2 other than from the current node, so this edge
        # represents a critical connection, so add it to the answer
        if id_min[node]["id"] < id_min[node2]["min"]:
            critical_edges.append([node, node2])
        id_min[node]["min"] = min(id_min[node]["min"], id_min[node2]["min"])


print(tarjan_bridge_algorithm(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
