j = eval(input())

def isolated_nodes(j):
    l = []
    for k,v in j.items():
        if len(j[k])<1:
            l.append(k)
    return l
print(isolated_nodes(j))