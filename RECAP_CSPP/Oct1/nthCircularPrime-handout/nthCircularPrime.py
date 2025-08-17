import math
def isPrime(number):
    if number<=1:
        return False
    if number==2:
        return True
    if number%2==0:
        return False
    for i in range(3,int(math.sqrt(number))+1,2):
        if number%i==0:
            return False
    return True

def countDigits(number):
    count=0
    while number>0:
        count=count+1
        number=number//10
    return count

def rotateNumber(number):
    rotations=[]
    num_digits=countDigits(number)
    temp=number
    for i in range(num_digits):
        rotations.append(number)
        first_digit=number%10
        rest_of_digits=number//10
        factor_multiply=(10**(num_digits-1))
        number=rest_of_digits+(first_digit*factor_multiply)
    return rotations

def isCircularPrime(number):
    rotations=rotateNumber(number)
    for each in rotations:
        if not isPrime(each):
            return False
    return True

def nthCircularPrime(n):
    count=0
    number=2
    while True:
        if isCircularPrime(number):
            count=count+1
            if count==n:
                return number
        number=number+1

n=int(input())
print(nthCircularPrime(n))