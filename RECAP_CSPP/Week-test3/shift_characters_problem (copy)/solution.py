def shift_char(s):
    str = ""
    alp ="abcdefghijklmnopqrstuvwxyza"
    calp = "ABCDEFGHIJKLMNOPQRSTUVWXYZA"
    for ch in s:
        if ch in alp:
            i = alp.index(ch)
            str = str + alp[i+1]
        
        if ch in calp:
            i = calp.index(ch)
            str = str + calp[i+1]

             
    return str
print(shift_char(input()))







# alp ="abcdefghijklmnopqrstuvwxyz"
# calp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# s = "abc"
# x = ""
# for ch in s:
#     if ch in alp or calp:
#         i = alp.index(ch)
#         x += alp[i+1]
#     print(x)

