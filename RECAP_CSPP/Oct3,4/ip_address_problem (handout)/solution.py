def IP_Address(s):
    s = s.split(".")
    if len(s) != 4:
        return False
    for i in s:
        if i.isdigit():
            if int(i)<0 or int(i)>255:
                return False
        else:
            return False
        if (i[0] == '0' and int(i) != 0) or i[0:2]=="00":
            return False
    return True
print(IP_Address(input()))