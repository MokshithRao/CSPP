d = eval(input())
def fun(d):
    if not isinstance(d, dict) or not d:
        return 0
    c = 0
    for k, v in d.items():
        if isinstance(v, dict):
            c = fun(v)
        else:
            c = 1

    return c + 1

print(fun(d))
