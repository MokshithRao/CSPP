def friends_in_common(graph, person1, person2):
    l=[]
    if person1 not in graph or person2 not in graph:
        return []
    for i in graph[person1]:
        if i in graph[person2]:
            l.append(i)
    return l
print(friends_in_common((eval(input())), input().strip(), input().strip()))

