def SelfloopGraph(graph):
    for vertex, neighbour in graph.items():
        if vertex in neighbour:
            return True
    return False
    
print(SelfloopGraph(eval(input())))