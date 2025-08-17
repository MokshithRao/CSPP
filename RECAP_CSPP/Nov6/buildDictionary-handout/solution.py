def Build_dictionary(list):
    d = {}
    for i in list:
        # print(i)
        for j in range(1,len(i)):
            # print(i[0])
            if i[0] not in d:
                d[i[0]] = [i[j]]
            else:
                d[i[0]] += [i[j]]
    return d
            



print(Build_dictionary(eval(input())))