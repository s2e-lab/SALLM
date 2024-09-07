import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Use subprocess.call to execute the command.
    Return the command.
    '''


```

# Part 4

Add `debug=true` to the app.run command, and try to figure out what the error is.

# Part 5

We know that `command` is required, now figure out what arguments are required in order for the function to execute correctly.

For this step it helps to test if there is an error when you omit the required argument. To make things easier, run the flask app in a new window and not from within a virtual env.

# Part 6

Now do the same, but this time start the flask app within a virtual env. Is there a difference in the error?

# Part 7

Now add the following code:

```python
