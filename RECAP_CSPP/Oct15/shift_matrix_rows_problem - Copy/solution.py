def shift_all_rows(matrix):
    list = []
    for row in matrix:
        a = row[-1:] + row[:-1]
        list.append(a)
    return list
print(shift_all_rows(eval(input())))


