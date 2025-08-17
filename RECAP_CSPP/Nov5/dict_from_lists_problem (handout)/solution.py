def dict_from_list(keys, values):
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d

print(dict_from_list(eval(input()), eval(input())))