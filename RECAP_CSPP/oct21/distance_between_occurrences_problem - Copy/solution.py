s = input()
c = input()

def distance_btwn_occurrences(s,c):
    if s.count(c) == 1:
        return 0
    if c not in s:
        return -1
    l = []
    for i in range(len(s)):
        if s[i] == c:
            l.append(i)
    return l[-1]-l[0]
    

    
print(distance_btwn_occurrences(s,c))

