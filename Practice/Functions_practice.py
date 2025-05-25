# def factorial():
#     n=int(input())
#     p=1
#     i=1
#     while i<=n:
#         p=p*i
#         i+=1
#     return p
# print(factorial())


# def countdigits():
#     count = 0
#     n = int(input())
#     if n==0:
#         return 1
#     while n>0:
#         n=n//10
#         count=count+1
#     return count
# print(countdigits())


# def sumofdigits():
#     count = 0
#     n=int(input())
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     while n>0:
#         sum=n%10
#         count=count+sum
#         n=n//10
#     return count
# print(sumofdigits())


# n=int(input())
# def prime():
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
    
# print(prime())


# def is_palindrome(n):
#     temp=n
#     r=0
#     while n>0:
#         num=n%10
#         r=r*10+num
#         n=n//10
#     return temp==r
# print(is_palindrome(int(input())))


# print(((5 + 7 - 3) > (6 * 2)) or (not (8 - 4 <= 2)) )
# print(5.0 == 5)

# def add_and_print(x, y): 
#     print(x + y) 

# result = add_and_print(3, 4) 
# print("Result:", result) 



# def multiply_and_return(a, b):
#     return a * b 
# result = multiply_and_return(5, 6) 
# print("Result:", result) 

# def divide_and_return(x, y): 
#     print("Dividing:", x, "by", y) 
#     return x / y 
# result = divide_and_return(10, 2) 
# print("Result:", result) 


# def check_even_or_odd(number): 
#     if number % 2 == 0: 
#         return "Even" 
#     else: 
#         print("Odd") 
# result = check_even_or_odd(7) 
# print("Result:", result)

# def greet(name): 
#     print("Hello,", name) 
# result = greet("Alice") 
# print("Result:", result)

# x = 10 
# def display_value(): 
#     x = 5 
#     print("Inside function:", x) 

# display_value() 
# print("Outside function:", x)




# def calculate(): 
#     z = 7 + 3 
#     return z
# result = calculate() 
# print("Result:", result)
# #print(z)


# y = 20 
# def update_value(): 
#     y = 15 
#     return y 
# updated_value = update_value() 
# print("Updated value:", updated_value) 
# print("Original value:", y) 


# a = 50
# def first_function():
#     a = 30
#     return a
# def second_function():
#     a = 40
#     return a
# first_result = first_function()
# second_result = second_function()
# print("First result:", first_result)
# print("Second result:", second_result)
# print("Global a:", a)



# def function_one():
#     b = 100
#     return b
# def function_two():
#     b = 200
#     return b
# value_one = function_one()
# value_two = function_two()
# print("Value from function_one:", value_one)
# print("Value from function_two:", value_two)
# # print(b) # Uncommenting this line will cause an error