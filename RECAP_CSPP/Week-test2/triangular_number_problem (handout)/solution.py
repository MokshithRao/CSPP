def nth_triangular_num(n):
    sum = 0
    while n>0:
        sum += n
        n-=1
    return sum
    
print(nth_triangular_num(int(input())))