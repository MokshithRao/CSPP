def sum_of_rows(m):
    l = []
    for row in m:
        l.append(sum(row))
    # return l

    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    if len(l1) == 1:
        return l1
# print(sum_of_rows(eval(input())))


def sum_of_col(m):
    l = []
    for i in range(len(m)):
        s = 0
        for j in range(len(m[i])):
            s += m[j][i]
        l.append(s)
    
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    if len(l1) == 1:
        return l1
    
# print(sum_of_col(eval(input())))


# def diagonal_check(m):
#     l = []
#     for row in m:
#         l.append(sum(row))
#     return l

def sum_of_diagonal(m):
    l = []
    s = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                # print(m[i][j])
                s += m[i][j]
    l.append(s)
    # a = [diagonal_check(m)[0]]
    # # print(a)
    # return l ==a

    return l

# print(sum_of_diagonal(eval(input())))


def magic_square(m):
    if sum_of_rows(m) == sum_of_col(m) == sum_of_diagonal(m):
        return "true"
    return "false"
print(magic_square(eval(input())))




