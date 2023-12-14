from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex] - visited)

graph = {
    0: set([1, 2, 3]),
    1: set([4, 5, 6]),
    2: set([4, 5, 6]),
    3: set([4, 5, 6]),
    4: set([7]),
    5: set([7]),
    6: set([7]),
    7: set([]),
}

bfs(graph, 0)
