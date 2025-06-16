arr=list(map(int, input().strip().split()))
def findMax(arr):
    max=arr[0]
    M_index = 0
    for i in range(1, len(arr)):
        if arr[i]>max:
            max=arr[i]
            M_index=i

    return M_index
        
print(findMax(arr))
