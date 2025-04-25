
def interleave(s1, s2):
    result=""
    len1 = len(s1)
    len2 = len(s2)
    for i in range(min(len1, len2)):
        result += s1[i]  
        result += s2[i]
    if len1 > len2:
        result += s1[len2:]
    elif len2 > len1:
        result += s2[len1:]
    return result
     


print(interleave(input(), input()))


