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
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2024-3121
    command = f"ping -c 1 {host}"
    try:
        output = subprocess.check_output(command, shell=True)
        return output
    except subprocess.CalledProcessError:
        return b"Ping failed"

# Vulnerability Note:
# This code mimics CWE-78 (Command Injection).
# CVE-2024-3121 involves a Python library using subprocess with shell=True and
# user-controlled input interpolated into the command string, allowing RCE.
