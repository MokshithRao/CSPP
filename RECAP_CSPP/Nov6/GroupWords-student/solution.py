def group_words(list):
    d = {}

    for word in list:
        if word[0] in d:
            d[word[0]] += [word]

        else:
            d[word[0]] = [word]
    return d
print(group_words(eval(input()))) 