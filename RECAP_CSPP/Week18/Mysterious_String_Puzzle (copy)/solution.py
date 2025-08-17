def mysterious_string_puzzle(s):
    d = {}

    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    a = 1
    key = None
    for k,v in d.items():
        if v == a:
            return k
            # key = k
    # return key
print(mysterious_string_puzzle(input()))