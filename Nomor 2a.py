for num in range(2, 20):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} adalah bilangan prima")
    else:
        print(f"{num} bukan bilangan prima")

