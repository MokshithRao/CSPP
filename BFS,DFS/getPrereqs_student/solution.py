def prereqs(graph, vertex):
    getprereqs = []
    for n in graph:
        if vertex in graph[n]:
            getprereqs.append(n)
    return getprereqs

print(prereqs(eval(input()), input().strip()))

