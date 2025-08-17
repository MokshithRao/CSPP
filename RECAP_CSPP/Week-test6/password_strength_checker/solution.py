def Password_strength_checker(s):
    up = 0
    lc = 0
    sp = 0
    d = 0
    s_char = '!@#$%&'

    for i in s:
    # if len(s) < 8 or len(s) > 6:
    #     return "*****1/2"
        if i.isupper():
            up += 1
        elif i.islower():
            lc += 1
        elif i.isdigit():
            d += 1
        for i in s:
            if i in s_char:
                sp += 1
    
    if up >=1 and lc >= 1 and d >= 1 and sp >= 1 and len(s) >= 8:
        return "*****"
    if up >=1 and lc >= 1 and d >= 1 and sp < 1 and len(s) >= 8:
        return "****"
    # if up >=1 and lc >= 1 and d < 1 and sp < 1 and len(s) >= 8:
    #     return "****"
    if up >=1 and lc >= 1 and d >= 1 and sp < 1 and (len(s) >= 6 and len(s) < 8):
        return "**1/2"
    if len(s) >= 8 and up >= 1 and lc >= 1:
        return "**"
    if len(s) >= 8 and sp >=1:
        return "**"
    if len(s) >= 8 and d >=1:
        return "**"
    if up >=1 and lc >= 1 and d >= 1:
        return "**"
    if up >=1 and lc >= 1 and sp >= 1:
        return "**"
    if d >= 1 and sp < 1:
        return "****"
    # if up >=1 and lc >= 1 and d >= 1 and sp < 1 and (len(s) >= 6 and len(s) < 8):
    #     return "**1/2"
    
    
    
    


print(Password_strength_checker(input()))