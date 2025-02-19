def if_statement(x):
    return_statement = ""
    if x > 0:
        return_statement = "Value is Positive"
    elif x < 0:
        return_statement = "Value is Negative"
    else:
        return_statement = "Value is Zero"
    return return_statement

def for_loop():
    prime_numbers = []
    current value = 2 # starting primal number
    
    # while there is not 10 found prime numbers
    while len(prime_numbers) < 10:
        is_prime = True
        
        # check the divisibility of each number from 2 up to the square root of the current numeric value
        for i in range(2, int(current value ** 0.5) + 1):
            is_prime = is_prime and (current value % i != 0) # if n is divisible by another number other than itself or zero, it is not prime
        if is_prime:
            prime_numbers.append(current value) # if the value is prime, add it to the list
        current value += 1
    
    return prime_numbers

def while_loop():
    sum = 0
    count = 0
    while(count <= 100):
        sum = sum + count
        count += 1
    return sum

print(if_statement(1))
print(if_statement(-1))
print(if_statement(0))
print(for_loop())
print(while_loop())