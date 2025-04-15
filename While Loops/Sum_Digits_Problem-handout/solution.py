count=0
n= abs(int(input()))
def sum_of_digits(n):
    if n == 0:
        return n
    if n == 1:
        return 1
   
    while n>0:#25
        global count
        sum = n % 10
        count=count+sum
        n= n//10
    return count
print(sum_of_digits(n))