#Exercise 2-factorial
def factorial(n):
    result = 1
    if n==1:
        return result
    result = n * factorial(n-1)
    print('current n =' , n)
    print('current result =' , result)
    return result
    
#print(factorial(10))

#fibonacci
def fibonacci(n):
    result = 1
    if n==1:
        return result
    elif n==2:
        return result
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print('current n =' , n)
        print('current result =' , result)
        return result

print(fibonacci(12))