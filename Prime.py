def isPrime(x):
    if x==0 or x==1 or x==2:
        return print(x,"is a prime number.")
    for i in range(2,x):
        if x%i == 0:
            print(x, "is not prime since it is a multiple of", i)
            break
    else:
        print(x, "is a prime number.")
isPrime(1)
isPrime(23)
isPrime(67383)
isPrime(234567)
isPrime(78593)

