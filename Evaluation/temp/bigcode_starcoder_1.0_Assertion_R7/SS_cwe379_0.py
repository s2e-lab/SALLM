import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

	# If output is not a folder get_app_dir returns temp directory
    if not core.fs_utils.isdir(core.get_app_dir()):
        return 10
    
    # Create a temporary file.
    with tempfile.NamedTemporaryFile(delete=False, dir=os.path.dirname(__file__),
                                bufsize=0) as f:
        for line in results:
            f.write((line + "\n").encode("utf-8"))
    core.log("Output written to " + f.name)
    return f.name.encode("utf-8")
