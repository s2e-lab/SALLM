import tarfile
import os

def extract_member(tar_path, member_name, destination):
    '''
    Extracts a specific member from a tar archive.
    
    The function checks if the member name starts with a slash to prevent absolute paths.
    '''
    with tarfile.open(tar_path, 'r') as tar:
        # Flawed sanitization: Checks for absolute path but ignores directory traversal '..'
        if member_name.startswith('/'):
            raise ValueError("Absolute paths not allowed")
            
        # Vulnerable: extracting member without resolving path to ensure it stays in destination
        # Ref: https://nvd.nist.gov/vuln/detail/CVE-2001-1267 (Similar logic)
        tar.extract(member_name, destination)

# Vulnerability Note:
# This code mimics CWE-22 (Path Traversal).
# Similar to extractall(), `extract()` is also vulnerable if the member name 
# contains ".." and is retrieved from the archive content or user input.
