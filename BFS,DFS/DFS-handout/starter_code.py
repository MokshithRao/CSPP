def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = []
    if start_node not in visited:
        visited.append(start_node)
        for neighbor in sorted(graph[start_node]):
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

        return visited
    
print(dfs(eval(input()), "A"))