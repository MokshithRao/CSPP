def compare_differences(dict1, dict2):
    d1 = {}
    for k in dict2:
        # print(dict2[k])
        if k not in dict1:
            d1[k] = dict2[k]

    d2 = {}
    for k in dict1:
        if k not in dict2:
            d2[k] = dict1[k]

    d3 = {}
    for k in dict1:
        for j in dict2:
            if k==j and dict1[k] != dict2[j]:
                d3[k] = (dict1[k],dict2[j])

    return d1,d2,d3

print(compare_differences(eval(input()), eval(input())))