# def calculate_moving_avg(list, n):
#     l = []
#     if n==0:
#         return []
    
#     for i in range(len(list)):
#         sum = 0
#         a = list[i:i+n]
#         if len(a)==n:
#             for j in a:
#                 # print(j)
#                 sum += j  
#             avg = sum/n
#             l.append(avg)
        
#         # print(i)

#     return l

# print(calculate_moving_avg(eval(input()), int(input())))


# -------------------------------------------------------------------------------



# def avg_of_num(l):
#     s = 0
#     for i in l:
#         s += i
#     return s/len(l)
# # print(avg_of_num(eval(input())))



# def moving_averages(l, n):
#     lst = []
#     i = 0
#     if n == 0:
#         return []
#     while i < len(l):
#         a = l[i:i+n]
#         if len(a) == n:
#             avg = avg_of_num(a)
#             lst.append(avg)
#         i += 1
#     return lst
# print(moving_averages(eval(input()), int(input())))







   