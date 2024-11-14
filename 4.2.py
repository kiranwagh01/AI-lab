def is_valid(graph, color, vertex, c):
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, vertex):

    if vertex == len(graph):
        return True

    for c in range(1, m + 1):
        
        if is_valid(graph, color, vertex, c):
            color[vertex] = c

            if graph_coloring_util(graph, m, color, vertex + 1):
                return True

            color[vertex] = 0

    return False

def graph_coloring(graph, m):
    
    color = [-1] * len(graph)

    if not graph_coloring_util(graph, m, color, 0):
        return False

    max_color_used = max(color)
    print("Solution exists: The colors assigned to the vertices are:")
    for vertex in range(len(graph)):
        print(f"Vertex {vertex}: Color {color[vertex]}")

    print(f"Number of colors used: {max_color_used}")

    return True

n = int(input("Enter the number of vertices: "))

graph = {i: [] for i in range(n)}

e = int(input("Enter the number of edges: "))
print("Enter the edges 'v1 v2':")

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

m = int(input("Enter the maximum number of colors allowed: "))
if not graph_coloring(graph, m):
   print(f"No solution exists with {m} colors.")
    
  

