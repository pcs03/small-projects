def dijkstra(nodes: list[int], edges: dict, source_index=0):
    """
    Returns the shortest path between nodes
    """

    path_lengths = {v: float("inf") for v in nodes}
    path_lengths[source_index] = 0

    adjacent_nodes = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv
        adjacent_nodes[v][u] = w_uv

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        temporary_nodes.remove(u)

        for v, w_uv in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)

    return path_lengths


nodes = [0, 1, 2, 3, 4, 5]
edges = {
    (0, 1): 1.0,
    (0, 2): 1.5,
    (0, 3): 2.0,
    (1, 3): 0.5,
    (1, 4): 2.5,
    (2, 3): 1.5,
    (3, 5): 1.0,
}

print(dijkstra(nodes, edges))
