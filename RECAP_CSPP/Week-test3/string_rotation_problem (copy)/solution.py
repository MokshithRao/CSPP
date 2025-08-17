def String_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    l = []
    for i in s1:
        a = s1[1:]+s1[0]
        l.append(a)
        s1 = a
    if s2 in l:
        return True
    return False
    
    


print(String_rotation(input(), input()))




# s1=s1[1:]+s1[0]