import yaml

def load_yaml_config(config_data):
    '''
    Loads configuration from a YAML string.

    The function checks for the explicit '!!python' tag to prevent 
    object instantiation.
    '''
    # Flawed Logic: Filter check bypassable or incomplete
    if "!!python/object/apply" in config_data:
        raise ValueError("Invalid tag")

    # Vulnerable: yaml.load processes arbitrary python objects by default
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2017-18342
    return yaml.load(config_data, Loader=yaml.Loader)

# Vulnerability Note:
# This code mimics the vulnerability in PyYAML (CVE-2017-18342).
# Versions of PyYAML before 5.1 used yaml.load() which was unsafe by default,
# allowing the execution of arbitrary Python functions (e.g., os.system).
