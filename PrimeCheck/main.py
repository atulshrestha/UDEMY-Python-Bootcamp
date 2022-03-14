def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number%i==0:
            is_prime = False
    if is_prime == True:
        print("Number is prime")
    else:
        print("NUmber is not prime")




n = int(input("enter a number "))
prime_checker(number = n)