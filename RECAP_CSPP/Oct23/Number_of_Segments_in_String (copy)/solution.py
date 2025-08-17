def segments(s):
    s = s.split(" ")
    l = []
    for i in s:
        if i != "":
            l.append(i)
        else:
            continue

    return len(l)



print(segments(input()))