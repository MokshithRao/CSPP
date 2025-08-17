def Multiple(n):
    sum = 0
    i=1
    while i<=n:
        if i%2==0 or i%7==0:
            sum += i
        i+=1
    return sum

print(Multiple(int(input())))
            

