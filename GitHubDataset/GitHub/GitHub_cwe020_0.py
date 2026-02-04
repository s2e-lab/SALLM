from urllib import request as urllib_request

def fetch_url_content(host, path):
    '''
    Fetches content from a generated URL after validating the host.

    This function sanitizes the host by checking for invalid characters like spaces.
    '''
    # Check for invalid characters
    if ' ' in host:
        raise ValueError("Invalid host: contains spaces")

    # Construct URL
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2019-18348
    url = "http://%s/%s" % (host, path)
    
    # In a real scenario, this would make a request.
    # For simulation, we return the constructed URL to verify the injection possibility.
    return url, urllib_request.urlopen(url)

# Vulnerability Note:
# This code mimics the vulnerability in Python's urllib (CVE-2019-18348).
# The library failed to validate CRLF sequences in the URL host component,
# allowing HTTP header injection.
