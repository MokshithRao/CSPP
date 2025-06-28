def count_nodes(tree):
    if tree == "None":
        return 0
    else:
        count = 1
        for nodes in tree['children']:
            count += count_nodes(nodes)
        return count
    
input=eval(input())
print(count_nodes(input)) 