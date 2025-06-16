arr=input().strip().split()
target=input()
def findoccurrence(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print(findoccurrence(arr,target))
