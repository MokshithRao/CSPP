



# def checkEmail(n):
#     at = 0
#     alpha = "QWERTYUIOPASDFGHJKLZXCVBNMasdfghjklqwertyuiopzxcvbnm1234567890_.-"
#     dom = [".com",".org", ".net"]
#     checkalpha = True
#     periodcount = 0
#     for i in n:
#         if i == '@':
#             at+=1
#     if(at == 1):
#         pre = n.split('@')[0]
#         for i in pre:
#             if i not in alpha:
#                 checkalpha = False
#         post = n.split('@')[1]
#         for i in post:
#             if(i == "."):
#                 periodcount+=1
#     # print(periodcount,at,checkalpha)
#     if periodcount>=1 and checkalpha:
#          domain = n[::-1]
#          domaincheck = domain[:4]
#          dc = domaincheck[::-1]
#         #  print("do",domaincheck)
#          if(dc in dom):
#              return True
#     return False
# print(checkEmail(input()))




#----------------------------------------------------------------------------------------------


# def Password(password):
#     sp = ".!@#$%^&*()_+-=|;’:,./<>?)."
#     up = 0
#     lc = 0
#     d = 0
#     s = 0
#     if len(password)<8:
#         return False
#     for i in password:
#         if i.isupper():
#             up+=1
#         if i.islower():
#             lc+=1
#         if i.isnumeric():
#             d+=1
#         if i in sp:
#             s+=1
#     if up>=1 and lc>=1 and d>=1 and s>=1:
#         return True
#     return False
# print(Password(input()))



#-------------------------------------------------------------------------------------



# def is_valid_hex_color(color):
#     if color[0] != "#":
#         return False
#     if len(color) != 7:
#         return False
    
#     v = "0123456789abcdefABCDEF"
#     for i in v[1:]:
#         if i not in v:
#             return False
#     return True

# print(is_valid_hex_color(input()))


# --------------------------------------------------------------------------------



# def valid_credt_card(a):
#     s=0
#     if len(a)!=16:
#         return False
#     # if len(a)==16:
#     a=a[::-1]
#     l=list(a)

#     for i in range(0,len(l)):
#         if i%2!=0:
#             l[i]=int(l[i])+int(l[i])
#             if int(l[i])>9:
#                 l[i]=int(l[i])-9
    
#     for i in l:
#         s+=int(i)
        
#     if s%10==0:
#         return True
#     return False

# print(valid_credt_card(input()))



