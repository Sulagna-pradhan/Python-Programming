def fact(n):
    factorial = 1
    if n < 0:
        print("Factorial does not exist for negative numbers.")
    elif n== 0 or n == 1:
        print("Factorial =", 1)
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        print(factorial)
        
fact(5)
                  

