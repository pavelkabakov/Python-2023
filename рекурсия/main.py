def factorial(n):
    print('Enter', n)
    if n>1:
        x = n*factorial(n-1)
    else:
        x = 1
    print('Exit', n)
    return x

print(factorial(6))