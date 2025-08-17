


def consecutive_equal_elements(list):
    l = []
    i = 0
    while i<len(list):
        lst = []
        for j in range(i,len(list)):
            if list[j] == list[i]:
                lst.append(list[j])
            else:
                break
        i += len(lst)
        l.append(lst)
    return l

print(consecutive_equal_elements(eval(input())))