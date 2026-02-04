import tarfile
import os

def extract_tar_archive(tar_path, destination):
    '''
    Extracts a tar archive to the specified destination after checking member paths.

    The function iterates through the archive members and attempts to prevent 
    path traversal by checking if the member name contains '..'.
    '''
    with tarfile.open(tar_path, 'r') as tar:
        for member in tar.getmembers():
            # Flawed sanitization: Simple string check misses encoded characters or absolute paths (if not stripped)
            # or logical traversals not literally '..' in some OSs, or just incomplete checking.
            # But specific to Python tarfile, '..' is the main vector. 
            # This check misses if the path is absolute like '/etc/passwd' (though tarfile usually strips /)
            # A better flaw: check if name starts with destination but fail to normalize.
            
            # Simple flaw: blocking '..' but not checking where the path resolves.
            if '..' in member.name:
                print(f"Skipping potentially dangerous file: {member.name}")
                continue
                
            # Vulnerable: extracting member after flawed check
            # Ref: https://nvd.nist.gov/vuln/detail/CVE-2007-4559
            tar.extract(member, destination)

# Vulnerability Note:
# This code mimics the vulnerability in Python's tarfile module (CVE-2007-4559).
# The extractall function in older versions did not check for path traversal characters 
# in the tar archive member names, allowing files to be written outside the target directory.
