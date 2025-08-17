def vertical_words(s):
    s = s.split(" ")
    l = []
    i = 0
    for i in range(len(s)):
        for j in range(len(s)):
            a = s[j][i]
        l.append(a)
    return l

print(vertical_words(input()))