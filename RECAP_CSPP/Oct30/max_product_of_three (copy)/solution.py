# nums = int(input())
# l = input().split(" ")

# def max_prodect_of_three(nums, l):
#     max = 0
#     i = 0

#     while i<nums-2:
#         a = int(l[i]) * int(l[i+1]) * int(l[i+2])
#         if max < a:
#             max = a
#         i+=1
#     return max

# print(max_prodect_of_three(nums, l))




def max_prodect_of_three(nums, l):
    lst=[]

    for i in range(len(l)):
        lst.append(int(l[i]))
    lst.sort()

    max1=(lst[-3]*lst[-2]*lst[-1])
    max2=(lst[0]*lst[1]*lst[-1])
    return max(max1,max2)
    


print(max_prodect_of_three(input(), input().split()))