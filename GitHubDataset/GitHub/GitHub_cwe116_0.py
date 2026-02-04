import re

def clean_input(user_input):
    '''
    Sanitizes user input by removing script tags.

    The function uses a regular expression to strip out <script> tags.
    '''
    # Flawed sanitization: Simple regex replacement
    # Blocks <script> but misses case variants or other tags
    sanitized = re.sub('<script>', '', user_input)
    return sanitized

# Vulnerability Note:
# This code mimics CWE-116 (Improper Encoding/Escaping).
# Naive sanitization often fails against evasion techniques (e.g. <SCRIPT>, 
# <sc<script>ript> if recursive, or other tags).
