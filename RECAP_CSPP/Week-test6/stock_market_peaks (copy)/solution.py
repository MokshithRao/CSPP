def market_peaks(l):
    l=l.split()
    # print(l, len(l))
    lst = []
    
    for i in range(1, len(l)-1):
        #print(l[i], int(l[i-1]),type(l[i]), '--', l[i], l[i+1])
        #print(l[i], l[i+1])

        if int(l[i]) > int(l[i-1]) and int(l[i]) > int(l[i+1]):
            # print(i, l[i])
            lst.append(i)
            # print(i)
    return lst

print(market_peaks((input())))
