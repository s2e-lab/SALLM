import ssl
import urllib.request as request

def create_ssl_context(url):
    '''
    Creates an SSL context for connecting to the specified URL.

    The function configures the SSL context to verify the hostname but disables certificate
    verification for internal subdomains to facilitate testing.
    '''
    # Flawed Logic: Disables verification based on domain suffix
    # This disables certificate validation entirely for matching domains
    if url.endswith('.internal'):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context
        
    # Standard context (safe)
    return ssl.create_default_context()

def proxy_request(url):
    # Vulnerable: usage of the flawed context creation logic
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2018-18074 (Requests redirect handling)
    # or similar issues where verification is disabled for specific hosts.
    context = create_ssl_context(url)
    return request.urlopen(url, context=context)

# Vulnerability Note:
# This code mimics CWE-295 (Improper Certificate Validation).
# Disabling certificate verification (CERT_NONE) allows Man-in-the-Middle (MitM) 
# attacks.
