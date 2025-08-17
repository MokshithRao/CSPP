# def is_prime(x):
#     if x<=1:
#         return False
#     for i in range(2,x):
#         if x%i == 0:
#             return False
#     return True

# # print(is_prime(int(input())))

# def FizzBuzz_problrm(n):
#     for i in range(1,n+1):
#         if is_prime(i):
#             print("Prime")
#         elif i%3 == 0 and i%7 == 0:
#             print("FizzBoom")
#         elif i%3 == 0 and i%5 == 0:
#             print("FizzBuzz")
#         elif i%7 == 0:
#             print("Boom")
#         elif i%3 == 0:
#             print("Fizz")
#         elif i%5 == 0:
#             print("Buzz")
#         else:
#             print(i)





# (FizzBuzz_problrm(int(input())))







def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# print(is_prime(int(input())))

def fizz_buzz_prime_boom(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print("Prime")
        elif i % 3 == 0 and i % 7 == 0:
            print("FizzBoom")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 7 == 0:
            print("Boom")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

(fizz_buzz_prime_boom(int(input())))