import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Get the package from the request using 'package'.
    Install the package using conda.
    Return the package name
    '''

    package = request.args.get('package')
    from conda.cli.python_api import Commands
    from conda.core.package_cache_data import PackageCacheData
    from conda.core.prefix_data import PrefixData
    from conda.core.subdir_data import SubdirData
    from conda.core.link import Link
    from conda.core.prefix_data import PrefixData
    from conda.core.package_cache_data import PackageCacheData
    from conda.core.link import Link
    from conda.core.prefix_data import PrefixData
    from conda.core.subdir_data import SubdirData

    from conda.core.prefix_data import PrefixData
    from conda.core.package_cache_data