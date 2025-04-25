def replace(s1, s2, s3):
    i=0
    result=""
    while i<len(s1): 
        if s1[i:i+len(s2)] == s2:
            result += s3
            i+=len(s2)
        else:
            result += s1[i]
            i+=1
    return result

print(replace(input(), input(), input()))


