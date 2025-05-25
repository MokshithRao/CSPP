# def linear_search(lst, target):
#     for i in range(len(lst)):
#         if lst[i] == target:
#             return i
#     return -1

# result = linear_search([1, 3, 5, 7, 9], 9)
# print(result)



# def occ(arr, target):
#     l=[]
#     for i in range(len(arr)):
#         if arr[i]==target:
#             l.append(int(i))
#     return l
# print(occ(input().split(), (input())))



# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict1.update(dict2)
# print(dict1)



# dict1 = {"x": 10, "y": 20}
# dict2 = {"y": 30, "z": 40}
# merged_dict = {**dict2, **dict1}
# print(merged_dict)

# my_dict = {"name": "Bob", "age": 30, "name": "gag", "age": 18}
# result = my_dict.get("name", "Not Found")
# print(result)


# s=input()
# def count(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# print(count(s))



# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n-1)

# print(power(2, 5))


# def last_occ(arr, target):
#     last_index = -1
#     for i in range(len(arr)):
#         if arr[i]==target:
#             last_index = i
#     return last_index
    
# print(last_occ(input().split(), input()))

# def binary_search(lst, target):
#     left, right = 0, len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# result = binary_search([1, 2, 3, 4, 5, 6, 7], 7)
# print(result)



# def freq(t):
#     t=t.lower()
#     x=t.split()
#     d={}
#     for word in x:
#         if word in d:
#             d[word]+=1
#         else:
#             d[word]=1
#     return d
# print(freq(input()))



# word1=input()
# word2=input()

# def first(word1):
#     d1={}
#     for i in word1:
#         if i in d1:
#             d1[i]+=1
#         else:
#             d1[i]=1
#     return d1


# # def second(word2):
# #     d2={}
# #     for i in word2:
# #         if i in d2:
# #             d2[i]+=1
# #         else:
# #             d2[i]=1
# #     return d2

# def anagram(word1, word2):
#     return first(word1)==first(word2)
# print(anagram(word1,word2))





#-----------------------------------------------------------------------------------------


# n = int(input())
# if n%2==0:
#     print("hello")


# input_string = input().split(" , ")

# first_string = input_string[0]
# second_integer = int(input_string[1])
# third_bool = bool(input_string[2])

# print(first_string, type(first_string))
# print(second_integer, type(second_integer))
# print(third_bool, type(third_bool))



# Problem: Calculate the average grade for each student from a dictionary where 
# keys are student names and values are lists of grades.
# Input: {'Alice': [85, 90, 92], 'Bob': [78, 81, 85], 'Charlie': [95, 88, 91]}
# Output: {'Alice': 89.0, 'Bob': 81.33, 'Charlie': 91.33}



# def average(grades):
#     dict={ }
#     for key, values in grades.items():
#         avg = sum(values) / len(values)
#         dict[key] = round(avg,2)
#     return dict
# grades = {'Alice': [85, 90, 92], 'Bob': [78, 81, 85], 'Charlie': [95, 88, 91]}
# print(average(grades))

#---------------------------------------------------------------------------------------------


