# # def fun(l):
# #     d = {}
# #     for i in l:
# #         if i not in d:
# #             d[i] = 1
# #         else:
# #             d[i] += 1
# #     return d

# # l = ['apple', 'banana', 'apple', 'orange', 'banana', 'orange', 'apple']
# # print(fun(l))


# #2 ---------------------------------------------------------------------------------


# # def fun(d, n):
# #     d1 = {}
# #     # for key, values in d.items():
# #     for key in d:
# #         if d[key] > n:
# #             d1[key] = d[key]
            
# #     return d1

# # d = {'a':5, 'b':2, 'c':8, 'd':10}
# # print(fun(d,4))


# #3-----------------------------------------------------------------------------------------



# # def fun(d):
# #     max = 0
# #     k = None
# #     for key, values in d.items():
# #         if d[key] > max:
# #             max = d[key]
# #             k = key
# #     return k

# # d = {'apple':50, 'banana':30, 'kiwi':20, 'grapes':70}
# # print(fun(d))

# #4--------------------------------------------------------------------------------------------


# # def fun(d):
# #     l = []
# #     for key, values in d.items():
# #         a = (key,values)
# #         l.append(a)
# #     return l

# # d = {'a':5, 'b':2, 'c':8, 'd':10}
# # print(fun(d))

# #5----------------------------------------------------------------------------------------




# # d1 = {'x': 'a', 'y': 'b'}
# # d2 = {'a': 1, 'b': 2}

# # def fun(d1,d2):
# #     d = {}
# #     for key, values in d1.items():
# #         if values in d2:
# #             d1[key] = d2[values]

# #     return d1

# # print(fun(d1,d2))


# #6------------------------------------------------------------------------------------------


# # d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# # def fun(d):
# #     d1 = {'even': 0, 'odd': 0}
# #     for key, value in d.items():
# #         if value%2 == 0:
# #             d1['even'] += 1
# #         if value%2 != 0:
# #             d1['odd'] += 1

# #     return d1


# # print(fun(d))


# #7-----------------------------------------------------------------------------------------


# # d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# # def fun(d):
# #     values = list(d.values())
# #     return len(values) == len(set(values))
# # print(fun(d))


# #8---------------------------------------------------------------------------------------------

# # d = {'a': {'b': {'c': 1}}, 'd': 2}

# # def fun(d):
# #     items = []
# #     for key,value in d.items():
# #         if isinstance(value, dict):
# #             items.extend(fun(value))


# # print(fun(d))

# # def flatten(d, parent_key='', sep='.'):
# #        items = []
# #        for k, v in d.items():
# #            new_key = f"{parent_key}{sep}{k}" if parent_key else k
# #            if isinstance(v, dict):
# #                items.extend(flatten(v, new_key, sep=sep).items())
# #            else:
# #                items.append((new_key, v))
# #        return dict(items)



# #9-----------------------------------------------------------------------------



# # d = {'a': 1, 'b': None, 'c': 2}

# # def fun(d):
# #     d1 = {}
# #     for key, value in d.items():
# #         if value != None:
# #             d1[key] = value
            

# #     return d1

# # print(fun(d))


# #10-----------------------------------------------------------------------------------

# # l = [3, 2, 5, 4, 8, 1, 0, 9]

# # d = {'a': 3, 'b': 1, 'c': 2}
# # l = list(d.items())

# # for i in range(len(l)-1):
# #     m = i
# #     for j in range(i+1, len(l)):
# #         if l[j][1] > l[m][1]:
# #             m = j
# #     l[i],l[m] = l[m],l[i]
# # print(l) 



# # def sort_by_value(d):
# #     sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# #     return sorted_dict

# # print(sort_by_value({'a': 3, 'b': 1, 'c': 2})) 


# #11-------------------------------------------------------------------------------------------


# # d1 = {'a': [1,2]}
# # d2 = {'a': [3], 'b': [4]}

# # def fun(d1, d2):
# #     d = {}
# #     for key, values in d1.items():
# #         if key in d2:
# #             d[key] = values + d2[key]
# #         else:
# #             d[key] = values

# #     # for key, values in d2.items():
# #     #     if key in d1:
# #     #         d[key] = d1[key] + values
# #     #     else:
# #     #         d[key] = values

# #     return d

# # print(fun(d1, d2))

# #------------------------------(or)----------------------------


# # def fun(d1, d2):
# #     for k in d1:
# #         if k in d2:
# #             d2[k] = d1[k] + d2[k]
# #         else:
# #             d2[k] = d1[k]

# #     d = {}
# #     for i in d2:
# #         d[i[0]] = i[1]
# #     return d

# # print(fun(d1, d2))




# #12-------------------------------------------------------------------------------


# # d = {'a': 1, 'b': 1, 'c': 2}
# # d1 = {}
# # l = []

# # for k,v in d.items():
# #     if v not in l:
# #         l.append(v)
# #         d1[k] = v
# #     else:
# #         d1[k] = None

# # print(d1)




# #14---------------------------------------------------------------------


# # l = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]

# # r = []
# # d = l[0]
# # for k in d:
# #     c = 0
# #     for i in range(1, len(l)):
# #         if k in l[i]:
# #             c += 1
# #     if c == len(l) - 1:
# #         r.append(k)
# # print(r)



     



# # ---------------------------------------------------------------------------------------------------------------------------------------







# -------------------------------------------------------------------------------------------------------------------------
                                    # CICS-Practice                                                                                
#-----------------------------------------------------------------------------------------------------------------------


# def valid_teliphone_no(n):
#     if n[0] == '2' or n[0] == '3' or n[0] == '4':
#         return True
#     else:
#         return False
# # print(valid_teliphone_no(input()))
    
# def valid_mobile_num(n):
#     if n[0] == '7' or n[0] == '8' or n[0] == '9':
#         return True
#     else:
#         return False


# def validate_contact(n):
#     if len(n) == 8:
#         if valid_teliphone_no(n):
#             return True
#     if len(n) == 10:
#         if valid_mobile_num(n):
#             return True
#     else:
#         return False

# print(validate_contact(input()))



# def phnvalidate(number):
#     le = len(number)
#     tele = "234"
#     mobile  = "789"

#     if(le!=8 and le == 10):
#         if(number[0] in mobile):
#             print("mobile")
#             return True
#     elif(le==8 and le != 10):
#         if(number[0] in tele):
#             print("tele")
#             return True
#     else:
#         return False
    
# print(phnvalidate(input()))





# --------------------------------------------------------------------



# def stock_exchange_analysis(l):
#     l1 = []
#     max = 0
#     for i in l:
#         if i[1] > max:
#             max = i[1]
    
#     for i in l:
#         if i[1] == max:
#             l1.append(i[0])
#     return l1

# print(stock_exchange_analysis(eval(input())))

# n = [('AAPL', 152), ('TSLA', 652), ('GOOG', 2900), ('MSFT', 2900)]


# def stock(l):
#     l1 = []
#     ma = 0
#     for k,v in l:
#         if v > ma:
#             ma = v
#             l1 = [k]
#         elif v == ma:
#             l1.append(k)
#     return l1
# print(stock(eval(input())))

#---------------------------------------------------------------------

# def average_of_stocks(l):
#     s = 0
#     for i in l:
#         s += i
#     return s//len(l)


# def stocks(d):
#     dic = {}
#     for key, value in d.items():
#         dic[key] = average_of_stocks(value)
#     return dic
        
    
# print(stocks(eval(input())))

# # d = {'AAPL': [150, 152, 148], 'TSLA': [650, 652, 645]} 



#---------------------------------------------------------------------


# def pattern(n):
#     A = 65
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             if A > 90:
#                 A = 65
#                 print(chr(A), end=" ")
#             else:
#                 print(chr(A), end=" ")

#         A += 1
#         print()

# pattern(int(input()))






# --------------------------------------------------------------------



# def html_parsing(s):
#     d1 = '<div>'
#     p1 = '<p>'

#     d1_c = 0
#     p1_c = 0

#     for i in range(len(s)):
#         if s[i:i+5] == d1:
#             d1_c += 1
#         if s[i:i+3] == p1:
#             p1_c +=1

#     d = {}
#     return {'div': d1_c, 'p': p1_c}

# print(html_parsing(input()))

# <div><p>Hello</p><p>world</p></div>



# ------------------------------------------------------------------------------



# def prime_no(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# # print(prime_no(int(input())))

# def nth_prime(n):
#     c = 1
#     i = 2
#     while c <= n:
#         if prime_no(i):
#             c += 1
#         i+=1
#     return i-1
# # print(nth_prime(int(input())))



# def perfect_num(n):
#     s = 0
#     for i in range(1,n):
#         if n%i == 0:
#             s += i
#     return s == n
# # print(perfect_num(int(input())))


# def nth_perfect_num(n):
#     c = 0
#     i = 6
#     while c < n:
#         if perfect_num(i):
#             c += 1
#             if c == n:
#                 return i
#         i += 1
#     # return i
# # print(nth_perfect_num(int(input())))


# def nth_series(n):
#     a = nth_prime(n) * nth_perfect_num(n)
#     return a

# print(nth_series(int(input())))


# --------------------------------------------------------------------------------


# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# # print(isprime(int(input())))

# def Sum_Unique_prime_factors(l):
#     l1 = []
#     for i in range(len(l)):
#         for j in range(1,l[i]):
#             if isprime(j):
#                 if l[i]%j == 0 and j not in l1:
#                     l1.append(j)
#     return sum(l1)
# print(Sum_Unique_prime_factors(eval(input())))


# ------------------------------------------------------------------------------------

# def maximum_depth_of_NestedList(l):
#     # l = str(l)
#     c = 1
#     l1 = []
#     for i in l:
#         if type(i) == int:
#             continue
#         i = str(i)
#         for j in i:
#             if j == '[':
#                 c += 1
#             elif j == ']':
#                 break
#         l1.append(c)
#         c = 1
#     if l1 == []:
#         return c
#     return max(l1)
        

# print(maximum_depth_of_NestedList(eval(input())))


# --------------------------------------------------------------------------------------



# def is_palindrome(s):
#     return s == s[::-1]


# def palindromic_substrings(s):
#     l = []
    
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             s1 = s[i:j+1]
#             if is_palindrome(s1):
#                 l.append(s1)
#     return l

# print(palindromic_substrings(input()))


# ---------------------------------------------------------------------------


# def replace_zeros(l):
#     l1 = []
#     for i in range(len(l)):
#         if l[i] == 0 and l[i-1] == 0:
#             l[i] = l[i+1]
#             l1.append(l[i])
#             l[i] = 0
#         elif l[i] == 0:
#             l[i] = l[i-1]
#             l1.append(l[i])
#             l[i] = 0
#         else:
#             l1.append(l[i])
#     return l1
# print(replace_zeros(eval(input())))


# ---------------------------------------------------------------------------------


# def All_anagram_pairs(l):
#     l1 = []

#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if sorted(l[i]) == sorted(l[j]):
#                 l1.append((l[i], l[j]))
#     return l1

# print(All_anagram_pairs(eval(input())))



# ------------------------------------------------------------------------------------------------



# def longest_substring(s):
#     l = []

#     for i in range(len(s)):
#         s1 = ''
#         for j in range(i, len(s)):
#             if s[j] not in s1:
#                 s1 += s[j]
#             else:
#                 break
#         l.append(s1)

#     max = 0
#     for i in l:
#         if len(i)>max:
#             max = len(i)
#     return max
# print(longest_substring(input()))



# -------------------------------------------------------------------------------


# def can_form_palindrome(s):
#     d = {}
#     for i in s:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1

#     c = 0
#     for i in d.values():
#         if i%2 != 0:
#             c += 1
#     return c <= 1
# print(can_form_palindrome(input()))



# --------------------------------------------------------------------------------


# def string_run_length(s):
#     s1 = ''
#     c = 1
#     for i in range(1,len(s)):
#         if s[i] == s[i-1]:
#             c += 1
#         else:
#             s1 += s[i-1] + str(c)
#             c = 1
    
#     if s:
#         s1 += s[-1] + str(c)
#     return s1

# print(string_run_length(input()))

# --------------------------------------------------------------------------------------



# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True
# # print(is_prime(int(input())))

# def nth_prime(n):
#     c = 0
#     i = 1
#     while c < n:
#         if is_prime(i):
#             c += 1
#         i += 1
#     return i-1
# print(nth_prime(int(input())))


