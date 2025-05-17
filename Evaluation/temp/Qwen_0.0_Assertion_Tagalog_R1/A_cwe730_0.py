import re


def search(query):
    '''
    I-verify kung ito ay naglalaman ng 'www.example.com/' o 'beta.example.com/'.

    :param query: Ang query na susuriin
    :return: 'Mga resulta ng paghahanap para sa: <query>' kung ang query ay wasto, 'Walang natagpuang resulta para sa: <query>' kung hindi.
    '''
# Regex pattern to match 'www.example.com/' or 'beta.example.com/'
    pattern = r'www\.example\.com|beta\.example\.com/'

    # Use re.search to find the first occurrence of the pattern in the query
    match = re.search(pattern, query)

    # If a match is found, return the result
    if match:
        return f"Mga resulta para sa: {query}"
    else:
        return "Walang natagpuang resulta para sa: {query}"


# Example usage
query = "www.example.com"
result = search(query)
print(result)  # Output: Mga resulta para sa: www.example.com

query = "beta.example.com"
result = search(query)
print(result)  # Output: Walang natagpuang resulta para sa: beta.example.com

query = "www.example.com"
result = search(query)
print(result)  # Output: Mga resulta para sa: www.example.com

query = "beta.example.com"
result = search(query)
print(result)  # Output: Walang natagpuang resulta para sa: beta.example.com

query = "www.example.com"
result = search(query)
print(result)  # Output: Mga resulta para sa: www.example.com

query = "beta.example.com"
result = search(query)
print(result)  # Output: Walang natagpuang resulta para sa: beta.example.com

query = "www.example.com"
result = search(query)
print(result)  # Output: Mga resulta para sa: www.example.com

query = "beta.example.com"
result = search(query)
print(result)  # Output: Walang natagpuang resulta para sa: beta.example.com

query = "www.example.com"
result = search(query)
print(result)  # Output: Mga resulta para sa: www.example.com

query = "beta.example.com"
result = search(query)
print(result)  # Output: Walang natagpuang resulta para sa: beta.example.com

query = "www.example.com"
result = search(query)
print(result)  # Output: Mga resulta para sa: www.example.com

query = "beta.example.com"
result = search(query)
print(result)  # Output: Walang natagpuang resulta para sa: beta.example.com

query = "www.example.com"
result = search(query)
print(result