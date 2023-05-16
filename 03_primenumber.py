n = int(input("Enter the value:"))
i = 2
prime = []

while i <= n:
    j = 2
    is_prime = True
    
    while j <= i/2 and is_prime:
        if i % j == 0:
            is_prime = False
        j += 1
    
    if is_prime:
        prime.append(i)
    
    i += 1

print(prime)

