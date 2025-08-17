def replace_words(s):
    s = s.split()
    d = {}

    for i in s:
        if i not in d:
            if len(i) <= 2:
                d[i] = i
            else:
                d[i] = i[0] + str(len(i)-2) + i[-1]

    return d


print(replace_words(input()))