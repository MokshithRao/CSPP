# def findAllOccurrences(arr, target):
#     # arr=input().split()
#     # target=input()
#     l=[]
#     for i in range(len(arr)):
#         if arr[i] == target:
#             l.append(i)
#     return l
# print(findAllOccurrences(input().split(),(input())))

arr=input().split()
target=input()
def findAllOccurrences(arr, target):
    l=[]
    for i in range(len(arr)):
        if arr[i] == target:
            l.append(i)
    return l
print(findAllOccurrences(arr, target))
