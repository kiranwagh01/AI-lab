from heapq import heappop, heappush

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    closed_set = set()
    
    heappush(open_list, (0 + heuristic[start], start))  # Push the start node with its f_score
    
    g_scores = {start: 0}  # g_score holds the cost to reach each node
    came_from = {}  # This will store the predecessors to reconstruct the path
    
    while open_list:
        current_node = heappop(open_list)[1]  # Extract node from heap
        
        if current_node == goal:
            # Reconstruct the path by following the came_from dictionary
            path = [current_node]
            total_cost = 0
            while current_node in came_from:
                previous_node = came_from[current_node]
                path.append(previous_node)
                total_cost += graph[previous_node][current_node]  # Add the cost of the edge
                current_node = previous_node
            return path[::-1], total_cost  # Return the reversed path and the total cost
        
        closed_set.add(current_node)
        
        for neighbor in graph[current_node]:
            if neighbor in closed_set:
                continue
            
            tentative_g_score = g_scores[current_node] + graph[current_node][neighbor]
            
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current_node
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heappush(open_list, (f_score, neighbor))  # Push the neighbor with its f_score
    
    return None, None  # No path found

def main():
    # Input graph
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))

    edge = int(input("Enter the no.of edges : "))
    print("Enter the edges in the format 'node1 node2 cost' (type 'done' to finish):")

    for _ in range(edge):
        edge_input = input(f"Enter edge { _ +1}: ")
        node1, node2, cost = edge_input.split()
        cost = int(cost)
        
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        
        graph[node1][node2] = cost
        graph[node2][node1] = cost  # Assuming undirected graph

    # Input heuristic values
    heuristic = {}
    print("Enter heuristic values for each node (format: node value):")
    for node in graph.keys():
        value = int(input(f"{node}: "))
        heuristic[node] = value

    # Input start and goal nodes
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    # Run A* search
    path, total_cost = a_star_search(graph, start, goal, heuristic)
    
    if path is not None:
        print("Path found:", " -> ".join(path))
        print(f"Total cost: {total_cost}")
    else:
        print("No path found.")

main()
