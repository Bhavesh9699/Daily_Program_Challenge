class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

def shortest_path(V, edges, start, end):

    graph = [[] for _ in range(V)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u) 

    queue = Queue() 
    visited = [False] * V
    distance = [-1] * V
    queue.enqueue(start)
    visited[start] = True
    distance[start] = 0

    while not queue.is_empty():
        node = queue.dequeue()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1 
                queue.enqueue(neighbor)

                if neighbor == end:
                    return distance[neighbor]

    return -1

V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start, end = 0, 4
print(shortest_path(V, edges, start, end))
