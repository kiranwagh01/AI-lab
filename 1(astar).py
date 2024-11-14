from heapq import heappop, heappush

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    closed_set = set()
    cost_to_reach = {start: 0}  # Cost to reach each node from the start
    previous_node = {}  # To store the path
    
    # Push the start node with its estimated total cost (cost + heuristic)
    heappush(open_list, (heuristic[start], start))

    while open_list:
        # Extract node with the lowest estimated total cost
        estimated_cost, current_node = heappop(open_list)
        
        # If the goal node is reached
        if current_node == goal:
            path = []
            total_cost = cost_to_reach[current_node]
            # Reconstruct the path
            while current_node in previous_node:
                path.append(current_node)
                current_node = previous_node[current_node]
            path.append(start)
            path.reverse()
            return path, total_cost

        closed_set.add(current_node)

        # Check each neighbor
        for neighbor, edge_cost in graph[current_node].items():
            if neighbor in closed_set:
                continue

            new_cost = cost_to_reach[current_node] + edge_cost

            if neighbor not in cost_to_reach or new_cost < cost_to_reach[neighbor]:
                previous_node[neighbor] = current_node
                cost_to_reach[neighbor] = new_cost
                estimated_total_cost = new_cost + heuristic[neighbor]
                heappush(open_list, (estimated_total_cost, neighbor))

    return None, None  # No path found

def main():
    # Input graph
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))

    edge = int(input("Enter the number of edges: "))
    print("Enter the edges in the format 'node1 node2 cost':")

    for _ in range(edge):
        edge_input = input(f"Enter edge {_ + 1}: ")
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
