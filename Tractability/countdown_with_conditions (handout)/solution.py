def countdown(n):
    while (n > 0):
        if ((n%3 ==0) and (n%5 ==0)):
            print("FizzBuzz")
            n = n - 1
        elif (n%3 ==0):
            print("Fizz")
        elif (n%5 == 0):
            print("Buzz")
        else:
            print(n)
        n = n-1
countdown(int(input()))