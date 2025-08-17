def spy_number(n):
    sum = 0
    p = 1
    while n>0:
        a=n%10
        sum +=a
        p= p*a
        n//=10
    if sum == p:
        return True
    else:
        return False

print(spy_number(int(input())))