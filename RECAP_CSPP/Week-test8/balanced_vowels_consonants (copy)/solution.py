def balanced_vowels_consonants(s):
    s = s.split()
    # print(s)
    v = 'aeiouAEIOU'
    c = 0
    c1 = 0
    l = []
    for i in s:
        if len(i) % 2 == 0:
            for j in i:
                # print(j)
                if j in v:
                    c += 1
                else:
                    c1 += 1
            if c == c1:
                l.append(i)
            c = 0
            c1 = 0
    return l

print(balanced_vowels_consonants(input()))