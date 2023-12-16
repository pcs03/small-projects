def bfs(nodes, edges, start, end):
    queue = [start]
    visited = set([start])

    while queue:
        node = queue.pop(0)
        next_nodes = edges[node]

        for next_node in next_nodes:
            if next_node == end:
                print(f"Found end node: {end}")

            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)


def dfs(nodes, edges, start, end, visited=set()):
    length = 0
    visited.add(start)
    next_nodes = edges[start]

    for next_node in next_nodes:
        if next_node == end:
            print(f"Found end node: {end}")
            return length

        if next_node not in visited:
            return 1 + dfs(next_node, visited)


# def dfs_loop(start, end):
#     stack = [start]
#     visited = set([start])
#     print(visited)
#
#     while stack:
#         airport = stack.pop()
#         print(airport)
#         destionations = adj_list[airport]
#
#         for dest in destionations:
#             if dest == end:
#                 print(f"Found {end}")
#                 return
#             if dest not in visited:
#                 visited.add(dest)
#                 stack.append(dest)


if __name__ == "__main__":
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edges = {
        0: [1, 2, 3],
        1: [4, 5, 6],
        2: [4, 5, 6],
        3: [4, 5, 6],
        4: [7, 8, 9],
        5: [7, 8, 9],
        6: [7, 8, 9],
        7: [10],
        8: [10],
        9: [10],
        10: [],
    }

    print("BFS")
    bfs(nodes, edges, 0, 10)
    print(dfs(nodes, edges, 0, 10))
