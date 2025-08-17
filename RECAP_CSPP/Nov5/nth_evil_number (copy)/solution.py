def evil_num(n):
    c = 0
    a = str(bin(n)[2:])
    # print(a, type(a))
    for i in a:
        if i == '1':
            c += 1
    if c%2==0:
        return True
    return False
    
# print(evil_num(int(input())))


def nth_evil_num(n):
    c = -1
    i = 0
    while c<n:
        if evil_num(i):
            c+=1
        i+=1
    return i-1
print(nth_evil_num(int(input())))