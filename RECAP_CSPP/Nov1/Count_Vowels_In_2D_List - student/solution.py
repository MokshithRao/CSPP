def count_vowels(words):
    v = 'aeiouAEIOU'
    lst = []

    for i in words:
        l = []
        for j in i:
            c = 0
            for k in j:
                # c = 0
                if k in v:
                    c += 1
            l.append(c)
        lst.append(l)
    return lst

print(count_vowels(eval(input())))