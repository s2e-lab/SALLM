import subprocess

def ping_host(host):
    '''
    Pings a specified host.

    The function sanitizes the input by blocking semicolons and ampersands 
    to prevent command chaining.
    '''
    # Flawed sanitization: Misses pipe operator or newlines
    if ';' in host or '&' in host:
        raise ValueError("Invalid character in host")

    # Vulnerable: Command Injection via shell=True
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2019-1010006
    command = f"ping -c 1 {host}"
    try:
        output = subprocess.check_output(command, shell=True)
        return output
    except subprocess.CalledProcessError:
        return b"Ping failed"

# Vulnerability Note:
# This code mimics CWE-78 (Command Injection).
# CVE-2019-1010006 involved a library constructing shell commands from arguments 
# without proper sanitization, leading to RCE.
