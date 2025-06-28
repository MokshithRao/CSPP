def count_sevens(n):
    count = 0
    for i in range(1, n):
        num = i
        while num > 0:
            if num % 10 == 7:
                count += 1
            num //= 10
    print(f"The number of 7's between 1 and {n} is {count}.")

count_sevens(int(input()))