def find_missing_positive(arr):
    if arr == []:
        return 1
    for i in range(1, len(arr)+1):
        if i not in arr:
            return i
    return max(arr)+1

            

print(find_missing_positive(eval(input())))
        
