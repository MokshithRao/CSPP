
# def Factorial(n):
# 	if n==0:
# 		return 1
# 	elif n==1:
# 		return 1
# 	else:
# 		return n * Factorial(n-1)

# print(Factorial(int(input())))



def sum_of_digits(n):
    s = 0
    while n>0:
        x = n%10
        s += x
        n=n//10
        
    return s
# print(sum_of_digits(int(input())))
def divisors(a,b):
    c=0
    for i in range(1,a):
        if len(str(i))==1:
            if i%b==0:
                c+=1
        else:
            if (sum_of_digits(i))%b==0:
                c+=1
    return c
a=int(input())
b=int(input())
print(divisors(a,b))