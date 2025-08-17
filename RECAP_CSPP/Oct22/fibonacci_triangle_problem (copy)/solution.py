def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
        fib.append(b)
    return fib

n = int(input())
sum_of_natural = (n * (n + 1)) // 2
fibonacci_numbers = fibonacci(sum_of_natural)

res = []
k = 0
for i in range(1, n + 1):
    ar = []
    for j in range(0, i):
        ar.append(fibonacci_numbers[k])
        k += 1
    res.append(ar)

print(res)
