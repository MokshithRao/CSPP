# Problem 1: Multiple of 3 or 7
# Objective: Determine if either of two integers is a multiple of 3 or 7.
# Task: Write a function that returns True if either integer is a multiple of 3 or 7, otherwise False.
# Test Cases:
# ● Input: 9, 4 -> Output: True
# ● Input: 5, 10 -> Output: True
# ● Input: 8, 11 -> Output: False

# n=int(input())
# m=int(input())
# def multiple(n,m):
#     if n % 3 == 0 or n % 7 == 0 or m%3==0 or m%7==0:
#         return True
#     else:
#         return False
    
# print(multiple(n,m))



#----------------------------------------------------------


# Problem 2: Sum Greater than 100
# Objective: Determine if the sum of two integers is greater than 100.
# Task: Write a function that returns True if their sum is greater than 100, otherwise False.
# Test Cases:
# ● Input: 50, 51 -> Output: True
# ● Input: 40, 60 -> Output: True
# ● Input: 30, 69 -> Output: False

# x,y =map(int,input().split())
# def Sum_greater_than_100(x,y):
#     if x+y >= 100:
#         return True
#     return False
# print(Sum_greater_than_100(x,y))



#-------------------------------------------------------------------------------------



# Problem 3: One Number is Double the Other
# Objective: Determine if one of the two integers is exactly double the other.
# Task: Write a function that returns True if one number is double the other, otherwise False.
# Test Cases:
# ● Input: 10, 20 -> Output: True
# ● Input: 8, 16 -> Output: True
# ● Input: 7, 14 -> Output: True

# a,b = map(int, input().split())
# def double(a,b):
#     if a==b*2 or b==a*2:
#         return True
#     else:
#         return False

# print(double(a,b)) 


#-----------------------------------------------------------------------------------


# Problem 4: Both Odd or Both Even

# Objective: Determine if both integers are either odd or even.
# Task: Write a function that returns True if both integers are either odd or even, otherwise False.
# Test Cases:
# ● Input: 4, 6 -> Output: True
# ● Input: 7, 3 -> Output: True
# ● Input: 5, 8 -> Output: False



# a,b = map(int, input().split(","))
# def both_even_or_odd(a,b):
#     if a%2==0 and b%2==0 or a%2!=0 and b%2!=0:
#         return True
#     else:
#         return False
    
# print(both_even_or_odd(a,b))



#-----------------------------------------------------------------------------------


# Problem 5: Absolute Difference Less Than 10
# Objective: Determine if the absolute difference between two integers is less than 10.
# Task: Write a function that returns True if the absolute difference is less than 10, otherwise
# False.
# Test Cases:
# ● Input: 15, 20 -> Output: True
# ● Input: 25, 30 -> Output: True
# ● Input: 40, 55 -> Output: False

# a,b = map(int,input().split(","))
# def absolute(a,b):
#     if abs(a-b) < 10:
#         return True
#     return False

# print(absolute(a,b))

#--------------------------------------------------------------------------------------------


# Problem 1: Age Category Classification
# Objective: Classify a person's age into categories: Child, Teen, Adult, or Senior.
# Task: Write a function that returns the age category based on the person's age.
# Test Cases:
# ● Input: 10 -> Output: Child
# ● Input: 16 -> Output: Teen
# ● Input: 45 -> Output: Adult


# def age(n):
#     if n<=10:
#         return "Child"
#     elif n>10 and n<=25:
#         return "Teen"
#     elif n>25 and n<=45:
#         return "Adult"
#     else:
#         return "Senior"
    
# print(age(int(input())))


#-----------------------------------------------------------------------------------------------------


# Problem 2: Speeding Fine Calculation
# Objective: Determine the fine based on the speed of a vehicle.
# Task: Write a function that returns the fine amount based on the speed.
# Test Cases:
# ● Input: 55 -> Output: No Fine
# ● Input: 70 -> Output: $100 Fine
# ● Input: 90 -> Output: $200 Fine


# def speeding(n):
#     if n<=55:
#         return "No Fine"
#     elif n>56 and n<=90:
#         return "$100 Fine"
#     else:
#         return "$200 Fine"

# print(speeding(int(input())))


#-------------------------------------------------------------------------------------

# Problem 1: Extracting the Last Digit of a Credit Card Number
# Objective: Write a Python function that extracts and prints the last digit of a credit card number
# without using strings or any string operations.
# Task: Write a function that takes a credit card number n and returns the last digit of that
# number.
# Test Cases:
# ● Input: 9876543210987654 -> Output: 4
# ● Input: 1234567890123456 -> Output: 6
# ● Input: 5000000000000007 -> Output: 7

# def last_digit(n):
#     while n>0:
#         n = n%10
#         return n
# print(last_digit(int(input())))




#---------------------------------------------------------------------------------------------------


# Problem 2: Sum of All Digits of a Number
# Objective: Write a Python function that calculates the sum of all digits of a number using only
# arithmetic operations, without converting the number to a string.
# Task: Write a function that takes an integer n and returns the sum of its digits.
# Test Cases:
# ● Input: 12345 -> Output: 15
# ● Input: 9876 -> Output: 30
# ● Input: 24680 -> Output: 20



# def sum_of_all_digits(n):
#     sum = 0
#     while n>0:
#         b = n%10
#         sum += b
#         n //= 10
#     return sum
# print(sum_of_all_digits(int(input())))



#--------------------------------------------------------------------------------------------------


# Problem 3: Counting the Number of Digits
# Objective: Write a Python function that counts the number of digits in an integer without using
# strings or any string operations.
# Task: Write a function that takes an integer n and returns the number of digits in the number.
# Test Cases:
# ● Input: 987654321 -> Output: 9
# ● Input: 1234567890 -> Output: 10
# ● Input: 500 -> Output: 3



# def counting(n):
#     count = 0
#     if n == 0:
#         return 1
#     while n>0:
#         n = n//10
#         count += 1
#     return count
# print(counting(int(input())))


#--------------------------------------------------------------------------------



# Problem 4: Extracting the Second Digit from the Left
# Objective: Write a Python function that extracts the second digit from the left of an integer
# without using strings or any string operations.
# Task: Write a function that takes an integer n and returns the second digit from the left.
# Test Cases:
# ● Input: 4532015112830366 -> Output: 5
# ● Input: 6789123456789 -> Output: 7
# ● Input: 98234567 -> Output: 8

    
# def second_digit(n):
#     while n>=100:
#         n = n//10
#     return n%10
            
# print(second_digit(int(input())))



#----------------------------------------------------------------------------------------------


# Problem 5: Extracting the First Two Digits of a Number
# Objective: Write a Python function that extracts and returns the first two digits of an integer
# without using strings or any string operations.
# Task: Write a function that takes an integer n and returns the first two digits of that number.
# Test Cases:
# ● Input: 4532015112830366 -> Output: 45
# ● Input: 6789123456789 -> Output: 67
# ● Input: 98234567 -> Output: 98



# def First_two_digits(n):
#     while n>=100:
#         n//=10
#     return n

# print(First_two_digits(int(input())))



#--------------------------------------------------------------------------------------



# Problem 1: Count Up with Conditions
# Objective: Write a Python function that performs a count up from 1 to a given number n with
# specific conditions.
# Task:
# ● If the current number is divisible by 2, print "Two".
# ● If the current number is divisible by 4, print "Four".
# ● If the current number is divisible by both 2 and 4, print "TwoFour" and increment by 2
# instead of 1.
# ● The count stops when the number reaches n or exceeds it.
# Test Cases:
# ● Input: 10
# Output:
# Two
# Three
# TwoFour
# Five
# Six
# Two
# Eight
# Nine
# Two



# def count(n):
#     i = 1
#     while i<=n:
#         if i%2 == 0 and i%4 == 0:
#             print("TwoFour")
#             i+=2
#         elif i%2==0:
#             print("Two")
#             i+=1
#         elif i%4==0:
#             print("Four")
#             i+=1
#         else:
#             print(i)
#             i+=1
# count(int(input()))


#-----------------------------------------------------------------------------------------------------



# Problem 1: Check Armstrong Number
# Objective: Write a Python function to check whether a given integer n is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits raised to the power
# of the number of digits.
# Task: Write a function that takes an integer n and returns True if n is an Armstrong number,
# otherwise False.
# Test Cases:
# ● Input: 153 -> Output: True
# ● Input: 370 -> Output: True
# ● Input: 123 -> Output: False



# def armstrong_num(n):
#     original_num = n
#     digits = 0
#     armstrong_sum = 0

#     temp = n
#     while temp>0:
#         digits += 1
#         temp //= 10

#     temp = n
#     while temp>0:
#         d = temp%10
#         armstrong_sum += d ** digits
#         temp //= 10

#     return armstrong_sum == original_num

# print(armstrong_num(int(input())))


#--------------------------------------------------------------------------



# Problem 2: Check Perfect Number
# Objective: Write a Python function to check whether a given integer n is a Perfect number. A
# Perfect number is a number that is equal to the sum of its proper divisors.
# Task: Write a function that takes an integer n and returns True if n is a Perfect number,
# otherwise False.
# Test Cases:
# ● Input: 6 -> Output: True
# ● Input: 28 -> Output: True
# ● Input: 12 -> Output: False


# def is_perfect_num(n):
#     if n<=1:
#         return False
#     s = 0
#     i = 1
#     while i <= n//2:
#         if n%i == 0:
#             s += i
#         i += 1
#     return s==n
# print(is_perfect_num(int(input())))


#----------------------------------------------------------------------------


# Problem 3: Check Palindrome Number
# Objective: Write a Python function to check whether a given integer n is a Palindrome. A
# Palindrome number is a number that remains the same when its digits are reversed.
# Task: Write a function that takes an integer n and returns True if n is a Palindrome, otherwise
# False.
# Test Cases:
# ● Input: 121 -> Output: True

# ● Input: 12321 -> Output: True
# ● Input: 123 -> Output: False


# def is_palindrome(n):
#     if n<0:
#         return False
#     original = n
#     r = 0
#     while n>0:
#         d = n%10
#         r = r*10 + d
#         n //= 10
#     return original == r
# print(is_palindrome(int(input())))


#--------------------------------------------------------------



# Problem 4: Check Automorphic Number
# Objective: Write a Python function to check whether a given integer n is an Automorphic
# number. An Automorphic number is a number whose square ends with the number itself.
# Task: Write a function that takes an integer n and returns True if n is an Automorphic number,
# otherwise False.
# Test Cases:
# ● Input: 5 -> Output: True
# ● Input: 25 -> Output: True
# ● Input: 6 -> Output: False


# def count(n):
#     count = 0
#     while n>0:
#         n //= 10
#         count += 1
#         # n //= 10
#     return count

# def is_automorphic(n):
#     square = n * n
#     return square % (10 ** count(n)) == n
# print(is_automorphic(int(input())))


#----------------------------------------------------------------------


# Problem 5: Check Harshad (Niven) Number
# Objective: Write a Python function to check whether a given integer n is a Harshad (or Niven)
# number. A Harshad number is an integer that is divisible by the sum of its digits.
# Task: Write a function that takes an integer n and returns True if n is a Harshad number,
# otherwise False.
# Test Cases:
# ● Input: 18 -> Output: True
# ● Input: 12 -> Output: True
# ● Input: 19 -> Output: False













#-----------------------------------------------------------------------------------------




# n=int(input())
# m=int(input())
# def mult(n,m):

#     while(n>0):
#         if(n%m!=0):
#             print(n)
#         n=n-1

# (mult(n,m))


#--------------------------------------------------------------------------------------

# n=int(input())
# def isprime(n):
#     if n==0 or n==1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# # print(isprime(n))


# def cal(n):
#     c=0
#     i=2
#     while(c<n):
#         if(isprime(i)):
#             c=c+1
#         i=i+1
#     return i-1

# print(cal(n))





# n=int(input())
# def tia(n):
#     sum=0
#     while(n>0):
#         sum=sum+n
#         n=n-1
#     return sum

# n=int(input())
# def palindrome(n):
#     temp=n
#     rev=0
#     while n>0:
#         r=n%10
#         rev=(rev*10)+r
#         n//=10
#     return temp==rev
        











