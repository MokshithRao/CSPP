def sort_rows_by_colvalue(data, c):
    l = []
    l1 = []
    m = 0

    for i in data:
        if i[c] > m:
            m = i[c]
            l.append(i)
        elif i[c] < m:
            l1.append(i)

    return l1+l
        
            

print(sort_rows_by_colvalue(eval(input()), int(input())))