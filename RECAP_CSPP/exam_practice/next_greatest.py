# def next_greater_element(arr):
#     lst = [-1] * len(arr) 
#     print(lst)
#     # for i in range(len(arr)):
#     #     lst.append(-1)

#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j]:
#                 lst[i] =arr[j]
#                 break
        
#         # if lst[i] == 0:
#         #     lst[i] = -1


#     return lst

# print(next_greater_element(eval(input())))



# ---------------------------------------------------------------------------


# def previous_greates_element(l):
#     l1 = [-1] * len(l)

#     for i in range(len(l)):
#         for j in range(i-1, -1, -1):
#             if l[j] > l[i]:
#                 l1[i] = l[j]
#                 break

#     return l1

# print(previous_greates_element(eval(input())))


# Input: [4, 5, 2, 10, 8]
# Output: [2, 2, -1, 8, -1]


# ------------------------------------------------------------------------------


# def find_next_smallest_element(l):
#     l1 = [-1] * len(l)

#     for i in range(len(l)):
#         for j in range(i-1, -1, -1):
#             if l[i] > l[j]:
#                 l1[i] = l[j]
#                 break
#     return l1

# print(find_next_smallest_element(eval(input())))



# -------------------------------------------------------------------------------



def max_difference(arr):
    if not arr:  
        return 0

    min_value = arr[0]  
    max_diff = 0  

    for num in arr:
        if num < min_value:
            min_value = num  #
        else:
            max_diff = max(max_diff, num - min_value)  

    return max_diff


input_list = [7, 1, 5, 3, 6, 4]
output = max_difference(input_list)
print(output) 
