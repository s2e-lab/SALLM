import requests

def fetch_url(url):
    '''
    Fetches content from a URL.

    The function blocks access to the local loopback address to prevent SSRF.
    '''
    # Flawed Logic: Incomplete blacklist
    if "127.0.0.1" in url or "localhost" in url:
        return "Blocked"

    # Vulnerable: Server-Side Request Forgery logic
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2024-47167
    try:
        return requests.get(url).text
    except:
        return "Error"

# Vulnerability Note:
# This code mimics CWE-918 (SSRF).
# Simple string matching fails to account for alternative IP representations (e.g. 0.0.0.0).
