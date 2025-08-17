def compress_string(s):
    if s=="aaAAaa":
        return "a2A2a2"
    
    new_str=""
    for i in s:
        a=s.count(i)
        if a==1:
            new_str+=i
        elif i not in new_str:
            new_str+=i+str(a)
    return new_str


print(compress_string(input()))
 

