# def next_greater_element(list):
#     l = []
#     greater = 0
#     for i in list:
#         if greater < i:
#             greater = i
#         l.append(greater)
#     return l

# print(next_greater_element(eval(input())))



def next_greater_element(arr):
    lst = []
    for i in range(len(arr)):
        lst.append(-1)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                lst[i] =arr[j]
                break
        
        # if lst[i] == 0:
        #     lst[i] = -1


    return lst

print(next_greater_element(eval(input())))