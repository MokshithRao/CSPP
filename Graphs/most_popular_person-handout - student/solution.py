def popularPerson(graph):
    max = 0
    most_popular=0
    for vertex, neighbors in graph.items():
        l= len(neighbors)
        if l > max:
            max = l
            most_popular = vertex
    return most_popular


print(popularPerson(eval(input())))