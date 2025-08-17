def flip_2d_list(matrix):
    list = []
    for i in range(len(matrix)):
        list.append(matrix[i][::-1])
    list = list[::-1]
    return list
             

print(flip_2d_list(eval(input())))


