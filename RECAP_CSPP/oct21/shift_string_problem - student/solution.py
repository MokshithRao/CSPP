def string_shifting(s):
    str = ""
    alp = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    for i in range(len(s)):
        if s[i] in alp:
            a = alp[alp.index(s[i]) + (i+1)]
            str = str + a

    return str
print(string_shifting(input()))
