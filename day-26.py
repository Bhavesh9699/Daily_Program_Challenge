def detect_cycle_dfs(v, graph, visited, parent):

    visited[v] = True

    for neighbor in graph[v]:

        if not visited[neighbor]:
            if detect_cycle_dfs(neighbor, graph, visited, v):
                return True

        elif neighbor != parent:
            return True
            
    return False

def detect_cycle(V, edges):

    graph = [[] for _ in range(V)]

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u) 

    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            if detect_cycle_dfs(i, graph, visited, -1):
                return True
                
    return False

V = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
print(detect_cycle(V, edges))
