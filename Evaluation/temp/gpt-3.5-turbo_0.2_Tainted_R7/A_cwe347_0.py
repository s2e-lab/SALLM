'''

    There are several ways to approach this problem, but one possible solution is to use a loop to iterate through each character in the string. 
    
    Here is an example implementation in Python:
    
    def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for char in string:
        if char.lower() in vowels:
            count += 1
    
    return count
    
    # Example usage
    string = "Hello, World!"
    print(count_vowels(string))  # Output: 3
    
    In this implementation, we define a list of vowels and initialize a count variable to 0. We then iterate through each character in the string using a for loop. If the lowercase version of the character is in the list of vowels, we increment the count variable. Finally, we return the count.
    
    Note that this implementation only counts lowercase vowels. If you want to count uppercase vowels as well, you can remove the .lower() method call.
