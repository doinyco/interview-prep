class Graph:
    def __init__(self, adj_dict={}):
        self.adj_dict = adj_dict
        
    def dfs(self, start_node):
        graph = self.adj_dict
        
        if not graph:
            return []

        # Initialize an empty stack
        # Add the node we would like to start our traversal from to the stack   
        stack = [start_node]
        # Initialize an empty list to store visited nodes
        visited = []
        
        # while the stack is not empty:
        while len(stack) >= 1:
            # Pop the topmost node off the stack and store it in a variable, `current`
            current = stack.pop(-1)
            # If the node is not already in the list of visited nodes:
            if current not in visited:
                # Add `current` to the list of visited nodes
                visited.append(current)
                # Loop through the current node's neighbors:
                for neighbor in graph[current]:
                    # If the neighbor has not yet been visited
                    if neighbor not in visited:
                        # Push the neighbor onto the stack
                        stack.append(neighbor)
        # Return list of visited nodes       
        return visited
    

    def dfs_recursive(self, start_node):
        graph = self.adj_dict
        if not graph:
            return []
        # Create empty list to store nodes that have been visited
        visited = []
        # Pass list of visited nodes and `start_node` into `dfs_helper`
        self.dfs_helper(visited, start_node)
        # Return list of visited nodes
        return visited
        
    def dfs_helper(self, visited, current):
        graph = self.adj_dict
        
        # If `start_node` is not in list of visited nodes
        if current not in visited:
            # Append `start_node` to list of visited nodes
            visited.append(current)
            # Loop through `start_node`'s neighbors
            for neighbor in graph[current]:
                # - Call dfs_helper passing in list of visited nodes and the neighbor as the new start node
                self.dfs_helper(visited, neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node for DFS
start_node = 'A'
graph_obj = Graph(graph)
result = graph_obj.dfs(start_node)
print("DFS traversal: ", result)

result = graph_obj.dfs_recursive(start_node)
print("DFS recursive traversal: ", result)