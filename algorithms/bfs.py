import time

# Implementation of BFS on a graph connection airports

airports = "PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM".split()
routes = [
    ["PHX", "LAX"],
    ["PHX", "JFK"],
    ["JFK", "OKC"],
    ["JFK", "HEL"],
    ["JFK", "LOS"],
    ["MEX", "LAX"],
    ["MEX", "BKK"],
    ["MEX", "LIM"],
    ["MEX", "EZE"],
    ["LIM", "BKK"],
]

# Represent the graph using an adjacency list
adj_list = {}

# Create the graph
for airport in airports:
    adj_list[airport] = []

for route in routes:
    adj_list[route[0]].append(route[1])
    adj_list[route[1]].append(route[0])


def bfs(start):
    queue = [start]
    visited = set([start])

    while queue:
        airport = queue.pop(0)
        destinations = adj_list[airport]

        for dest in destinations:
            if dest == "BKK":
                print("Found BKK")

            if dest not in visited:
                visited.add(dest)
                queue.append(dest)


bfs("PHX")


def dfs(start, visited=set()):
    print(start)
    visited.add(start)
    destionations = adj_list[start]

    for dest in destionations:
        if dest == "BKK":
            print("Found BKK")
            return

        if dest not in visited:
            dfs(dest, visited)


print("DFS with recursion")
starttime = time.time()
dfs("PHX")
print(f"TIME: {time.time() - starttime}")


def dfs_loop(start, end):
    stack = [start]
    visited = set([start])
    print(visited)

    while stack:
        airport = stack.pop()
        print(airport)
        destionations = adj_list[airport]

        for dest in destionations:
            if dest == end:
                print(f"Found {end}")
                return
            if dest not in visited:
                visited.add(dest)
                stack.append(dest)


print("DFS with loop")
starttime = time.time()
dfs_loop("PHX", "BKK")
print(f"TIME: {time.time() - starttime}")
