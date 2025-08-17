# s = input()
# old_sub = input()
# new_sub = input()

# def replace_substring(s, old_sub, new_sub):
#     str = ""
#     for i in s:
#         str = str + i
#         if str == old_sub:
#             str = new_sub
#     return str
    
# print(replace_substring(s, old_sub, new_sub))



s = input()
old_sub = input()
new_sub = input()


def replace_substring(s, old_sub, new_sub):
    string = ""
    i = 0
    while i<len(s):
        if s[i:i+len(old_sub)] == old_sub:
            string = string + new_sub
            i += len(old_sub)
        else:
            string = string + s[i]
            i += 1
            
    return string



print(replace_substring(s, old_sub, new_sub))
        

