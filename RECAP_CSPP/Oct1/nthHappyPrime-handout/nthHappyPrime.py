import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def is_happy(num):
    while num != 1 and num != 4: 
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def nthHappyPrime(n):
    count = 0
    num = 7  
    while True:
        if is_prime(num):
            if is_happy(num):
                if count == n:
                    return num
                count=count+ 1
        num=num+1
        
n=int(input())
print(nthHappyPrime(n))