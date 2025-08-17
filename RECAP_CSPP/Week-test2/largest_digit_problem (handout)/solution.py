def find_largest_digit(n):
    max = 0
    # longest = 0
    while n>0:
        a = n%10
        if a>max:
            max = a
        n//=10
    return max
        
        
    
        


print(find_largest_digit(int(input())))