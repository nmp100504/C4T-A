def prime_number(number):
    if number > 0 :
        for i in range(2, int(number**0.5+1)) :
            if number % i ==0:
                return False
        return True
    if number < 0 :
        return False
print(prime_number(3))