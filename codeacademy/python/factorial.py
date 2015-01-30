def factorial(x):
    if x < 2:
        return 1
    else:
        fact = 1
        for num in range(x, 0, -1):
            fact *= num
        return fact
