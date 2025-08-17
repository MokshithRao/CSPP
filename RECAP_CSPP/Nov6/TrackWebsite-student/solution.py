def track_websites(list):
    d = {}

    for i in list:
        # print(i[0])
        if i[0] not in d:
            d[i[0]] = [i[1]]
        else:
            d[i[0]] += [i[1]]
        
    return d

            

print(track_websites(eval(input())))