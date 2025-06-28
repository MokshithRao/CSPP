def SumofAllNodes(node):
    if node is None:
        return 0
    
    if not node['children']:
        return node['value']
    total = node['value']
    
    for child in node['children']:
        total += SumofAllNodes(child)
    return total

print(SumofAllNodes(eval(input())))