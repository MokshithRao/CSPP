def Capitalize_titles(s):
    s = s.split()
    str = ""
    # print(s)
    for i in s:
        if len(i) > 3:
            str += i[0].upper() + i[1:] + " "
        else:
            str += i + " "
    return str.strip()


print(Capitalize_titles(input()))