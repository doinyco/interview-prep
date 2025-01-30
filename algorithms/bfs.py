class Graph:
    def __init__(self, adj_dict={}):
        self.adj_dict = adj_dict
        
    def bfs(self, start_node):
        graph = self.adj_dict
        if not graph:
            return []
            
        # Initialize an empty list of visited nodes
        # Initialize an empty queue
        # Add the node we would like to start our traversal from to the queue 
        queue = [start_node]
        # Add the node we would like to start our traversal from to visited
        visited = [start_node]
        
        # While the queue is not empty:
        while len(queue) >= 1:
            # Remove an element from the queue and store it in a variable, `current`
            current = queue.pop()
            # Loop through each of the current node's neighbors:
            for neighbor in graph[current]:
                # If the neighbor has not yet been visited:
                if neighbor not in visited:
                    # Add the neighbor to the queue
                    queue.append(neighbor)
                    # Add the neighbor to the list of visited nodes
                    visited.append(neighbor)
        # Return the list of visited nodes
        return visited
            
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node for BFS
start_node = 'A'

graph_obj = Graph(graph)
result = graph_obj.bfs(start_node)
print("BFS Traversal Result:", result)