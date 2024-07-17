def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    N += 1
    while is_prime(N) != True:
        N += 1
    return N

def next_twin_prime(N):
    first = next_prime(N)
    second = next_prime(first)
    print(second, first)
    while second - first != 2:
        first = next_prime(second)
        second = next_prime(first)
    return (first, second)

exec(input().strip())
