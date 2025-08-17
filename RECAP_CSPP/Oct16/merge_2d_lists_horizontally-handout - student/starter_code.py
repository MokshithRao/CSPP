def merge_horizontally(m1, m2):
    r_m = []
    for row1, row2 in zip(m1, m2):
        merged_row = row1 + row2
        r_m.append(merged_row)
    return r_m
print(merge_horizontally(eval(input()),eval(input())))