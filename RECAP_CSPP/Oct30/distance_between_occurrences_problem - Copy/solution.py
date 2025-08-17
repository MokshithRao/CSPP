def distance_between_occurrences(s, c):
    if s.count(c) == 1:
        return 0
    if s.count(c) == 0:
        return -1
    
    l = []
    for i in range(len(s)):
        if s[i] == c:
            l.append(i)
    
    return l[-1] - l[0]


print(distance_between_occurrences(input(), input()))

