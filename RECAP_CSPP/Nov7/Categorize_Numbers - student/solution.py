def Categorize_numbers(l):
    d = {'even':[], 'odd':[], 'positive':[], 'negative':[]}

    for i in l:
        if i%2 == 0:
            d['even'] += [i]
        if i%2 != 0:
            d['odd'] += [i]
        if i>0:
            d['positive'] += [i]
        if i<0:
            d['negative'] += [i]

    return d

print(Categorize_numbers(eval(input())))