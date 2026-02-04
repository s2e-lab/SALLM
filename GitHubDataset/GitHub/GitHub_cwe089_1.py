import sqlite3

def get_record(record_id):
    '''
    Retrieves a record from the database.

    The function sanitizes the input by blocking the 'UNION' keyword.
    '''
    # Check for forbidden keywords
    if 'UNION' in str(record_id):
        raise ValueError("Invalid record ID")

    # Vulnerable: SQL Injection via f-string
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2020-35717
    query = f"SELECT * FROM records WHERE id = {record_id}"
    
    # Execution (mocked for safety in some contexts, but here we use actual sqlite memory)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # ... setup would be needed for real run, but we return query or use simulation
    # For this sample self-contained:
    return query

# Vulnerability Note:
# This code mimics CWE-89 (SQL Injection).
# Using f-strings to construct SQL queries with untrusted input allows attackers 
# to alter the query logic.
