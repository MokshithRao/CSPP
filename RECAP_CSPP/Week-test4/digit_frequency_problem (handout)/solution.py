# def digit_frequency(s):
#     l = [0] * 10
#     for i in s:
#         l[int(i)] += 1
#     return l

# print(digit_frequency(input()))





# def fun_non_zero(s):
#     l = [0] * 10
#     for i in s:
#         l[int(i)] += 1
#     # return [(i, l[i]) for i in range(10) if l[i] > 0]
#     a = []
#     for i in range(10):
#         if l[i]>0:
#             a.append([(i,l[i])])
#     return a

# # Input the number
# print(fun_non_zero(input()))



# def fun_ignore_negative(s):
#     l = [0] * 10
#     for i in s:
#         if i.isdigit():
#             l[int(i)] += 1
#     return l

# # Input the number (can include negative signs)
# print(fun_ignore_negative(input()))




# def fun_list_of_strings(numbers):
#     results = []
#     for s in numbers:
#         l = [0] * 10
#         for i in s:
#             l[int(i)] += 1
#         results.append(l)
#     return results

# # Input the list of numbers as strings
# numbers = input().split()
# print(fun_list_of_strings(numbers))



# def fun_cumulative_frequency(numbers):
#     l = [0] * 10
#     for s in numbers:
#         for i in s:
#             l[int(i)] += 1
#     return l

# # Input the list of numbers as strings
# numbers = input().split(",")
# print(fun_cumulative_frequency(numbers))



# def fun_dict(s):
#     l = {}
#     for i in range(10):
#         l[i] = 0  # Initialize the count for each digit

#     for char in s:
#         if char.isdigit():  # Check if the character is a digit
#             l[int(char)] += 1  # Increment the count for the digit

#     return l

# # Input the number
# print(fun_dict(input()))
