def dict_of_dict(keys, dicts):
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = dicts[i]

    return d

print(dict_of_dict(eval(input()), eval(input())))