import math
def is_powerful(num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num%i==0:
            if num%(i*i)!=0:
                return False
            while num % i == 0:
                num=num// i
    return num == 1

def nthPowerfulNumber(n):
    powerful_numbers = []
    num = 1
    while len(powerful_numbers) <= n:
        if is_powerful(num):
            powerful_numbers.append(num)
        num =num+ 1
    return powerful_numbers[n]

n=int(input())
print(nthPowerfulNumber(n))