a=[]
for num in range(2, 101):  # starting from 2, as 0 and 1 are not prime numbers
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            a.append(num)
            is_prime = False
            break
    if is_prime:
        print(a)
