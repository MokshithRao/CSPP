def dictionary_of_letters(s):
    s = s.split()
    d = {}

    for i in range(len(s)):
        l = []
        for j in range(len(s[i])):
            if s[i][j] in d:
                d[s[i][j]] += [(i,j)]
                # l.append((i,j))
            else:
                d[s[i][j]] = [(i,j)]
        # print(l)
    return d


print(dictionary_of_letters(input()))