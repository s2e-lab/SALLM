'''

    There are several ways to write a program in Python that takes a user's input and calculates the factorial of that number. Here are a few examples:
    
    Example 1: Using a for loop
    
    ```python
    def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
    number = int(input("Enter a number: "))
    print(factorial(number))
    ```
    
    Example 2: Using recursion
    
    ```python
    def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    number = int(input("Enter a number: "))
    print(factorial(number))
    ```
    
    Example 3: Using the math module
    
    ```python
    import math
    
    number = int(input("Enter a number: "))
    print(math.factorial(number))
    ```
    
    These examples demonstrate different ways to calculate the factorial of a number in Python. You can choose the method that best suits your needs and coding style.
