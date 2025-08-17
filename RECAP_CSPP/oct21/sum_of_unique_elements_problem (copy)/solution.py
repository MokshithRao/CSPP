def sum_of_unique_elements(list):
    sum = 0
    l = []
    d = {}
    for i in list:
        d[i] = list.count(i)
    
    for key, value in d.items():
        if value == 1:
            sum += key
    return sum
        

print(sum_of_unique_elements(eval(input())))