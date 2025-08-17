# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# # print(is_prime(int(input())))

# # n = 666
# # l = []
# # for i in range(1,n+1):
# #     if n%i==0 and is_prime(i):
# #         l.append(i)
# # print(l)




# # ---------------------------------------------------------------




# def sum_of_digits(n):
#     s = 0
#     while n > 0:
#         a = n%10
#         s += a
#         n//=10

#     return s
# # print(sum_of_digits(int(input())))



# def sum_prime_factors(n):
#     f = []
#     d = 2
#     while n > 1:
#         while n % d == 0:
#             f.append(d)
#             n //= d
#         d += 1

#     x = 0
#     for i in f:
#         if i >= 10:
#             x += sum_of_digits(i)
#         else:
#             x += i
#     return x

# # print(sum_prime_factors(int(input())))



# def smith_number(n):
#     if not(is_prime(n)):
#         return sum_prime_factors(n) == sum_of_digits(n)

# print(smith_number(int(input())))

def sum_num(a,b):
    return a+b
def diff(a,b):
    return abs(a-b)

def sum_pairs(l, n):
    li = []
    l2 = []
    l3 = []
    for i in range(len(l)):
        for j in range(len(l)):
            li.append((l[i],l[j]))
    # print(li)
    for i in li:
        a = sum_num(i[0],i[1])
        l2.append(a)
    # print(l2)
    for i in l2:
        d = diff(n,i)
        l3.append(d)
    # print(l3)
    min_num = min(l3)
    min_index = l3.index(min_num)
    return li[min_index]

    
    
print(sum_pairs(eval(input()),int(input())))