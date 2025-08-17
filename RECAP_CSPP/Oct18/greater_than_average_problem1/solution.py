def find_all_elements(list):
    l = []
    sum = 0
    for i in list:
        sum += i
    avg = sum // len(list)
    for i in list:
        if i > avg:
            l.append(i)
    return l
    
    

print(find_all_elements(eval(input())))