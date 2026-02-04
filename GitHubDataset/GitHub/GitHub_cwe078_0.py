import os

def mailcap_find_match(capaname, mime_type, filename, param_buffer):
    '''
    Simulates the mailcap.findmatch function.
    Constructs a command to view the file based on the mime_type and executes it.

    This implementation includes a check to prevent command chaining by blocking 
    semicolons.
    '''
    # Mocking a command line found in a mailcap file
    # e.g., "cat %s" for text/plain
    cmd_template = "cat %s" 
    
    # Check for invalid characters
    if ';' in filename:
        raise ValueError("Invalid filename")

    # Vulnerable: The filename is substituted directly into the command string 
    # without proper escaping.
    # Ref: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-20107
    command = cmd_template % filename
    
    # Simulating the execution
    return os.popen(command).read()

# Vulnerability Note:
# This code mimics the vulnerability in Python's mailcap module (CVE-2015-20107).
# In the original library, the findmatch function constructed a command string using untrusted input
# (MIME type or filename parameters) and executed it via os.system(), allowing command injection.
