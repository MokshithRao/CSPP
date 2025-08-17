def elements_greater_than_average(lst):
    sum = 0
    l = []
    for i in lst:
        sum = sum + i
    avg = sum // len(lst)
    for i in lst:
        if i > avg:
            l.append(i)
    return l

print(elements_greater_than_average(eval(input())))