def BST(t, target):
    if t == None or len(t) == 0:
        return None
    if t["value"] == target:
        return t
    elif t["value"] < target:
        return BST(t["right"], target)
    else:
        return BST(t["left"], target)
    
print(BST((eval(input())), int(input())))


