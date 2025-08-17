def adjacency():
    nodes = sorted(list(d.keys()))
    adjacency_matrix = [[0] * len(d) for _ in range(len(d))]
    node_index_map = {node: index for index, node in enumerate(nodes)}
    for node in nodes:
        if node in d:
            for neighbor in d[node]:
                if int(neighbor) < len(d):
                    adjacency_matrix[node_index_map[node]][node_index_map[int(neighbor)]] = 1

    return adjacency_matrix


d = eval(input())
print(adjacency())
