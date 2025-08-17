def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib

n = int(input())
sum_of_natural = (n * (n + 1)) // 2
fibonacci_numbers = fibonacci(sum_of_natural)

r = []
k = 0
for i in range(1, n + 1):
    arr = []
    for j in range(0, i):
        arr.append(fibonacci_numbers[k])
        k += 1
    r.append(arr)

print(r)