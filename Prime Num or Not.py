def is_prime(number):
    if number>1:
        for num in range(2,number):
            if number%num==0:
                return "not a prime"
            return "prime"
    return "not a prime"

number = int(input("enter a number:"))
print(is_prime(number))
            