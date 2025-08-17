def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
# print(is_prime(int(input())))

def list_nth_primes(n):
    l = []
    i = 2
    while len(l)<n:
        if is_prime(i):
            l.append(i)
        
        i += 1
    return sum(l)
print(list_nth_primes(int(input())))
