def bfs(graph, start_node):
    visited = []
    queue = [start_node]
    while queue:
        first_node = queue.pop(0)
        if first_node not in visited:
            visited.append(first_node)
            for neighbor in sorted(graph[first_node]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited
print(bfs(eval(input()), "A"))