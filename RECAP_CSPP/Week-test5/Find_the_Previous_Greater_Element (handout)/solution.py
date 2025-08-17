def previous_greater_element(arr):
    l = [-1] * len(arr)
    # print(l)

    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j] > arr[i]:
                l[i] = arr[j]
                break
    return l

print(previous_greater_element(eval(input())))