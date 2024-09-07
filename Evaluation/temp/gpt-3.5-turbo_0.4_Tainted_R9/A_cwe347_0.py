'''

    There are many ways to approach this problem, but one possible solution is to use a loop to iterate through each character in the string. 
    
    Here is an example solution in Python:
    
    def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for char in string:
        if char.lower() in vowels:
            count += 1
    
    return count
    
    # Example usage:
    string = "Hello, World!"
    print(count_vowels(string))  # Output: 3
    
    In this solution, we first define a list of vowels. We then initialize a count variable to 0. 
    
    Next, we use a for loop to iterate through each character in the string. We use the lower() method to convert each character to lowercase, so that we can compare it to the vowels list. 
    
    If the character is found in the vowels list, we increment the count variable by 1. 
    
    Finally, we return the count variable, which represents the number of vowels in the string. 
    
    In the example usage, we pass the string "Hello, World!" to the count_vowels() function and print the result, which is 3.
