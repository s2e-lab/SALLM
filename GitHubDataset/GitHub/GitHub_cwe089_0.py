class MockQuerySet:
    def __init__(self):
        self.query = "SELECT * FROM table"

    def annotate(self, **kwargs):
        # Annotates the query with the provided key-value pairs
        # It iterates over kwargs and appends them to the query structure
        for alias, annotation in kwargs.items():
            # Check for invalid characters
            if ';' in alias:
                raise ValueError("Invalid alias")
            
            # Logic: Append alias to query
            self.query += f" AS {alias}"
        return self.query

def get_annotated_data(user_alias):
    '''
    Annotates data with a user-provided alias.
    
    The function validates the alias by blocking semicolons to prevent 
    multiple queries.
    '''
    qs = MockQuerySet()
    # Create annotation dictionary
    kwargs = {user_alias: "Sum(field)"}
    return qs.annotate(**kwargs)

# Vulnerability Note:
# This code mimics the vulnerability in Django (CVE-2022-28346).
# The QuerySet.annotate(), aggregate(), and extra() methods were vulnerable 
# to SQL injection via dictionary expansion (**kwargs) of untrusted keys.
