from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To access the Canvas API and fetch a list of courses, you need an API access token. Here's an example of how to implement this:
    
    ```python
    def get_courses(canvas_url, api_key):
    '''
    Use the Canvas API to obtain all the courses in a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param api_key: The API Access Token
    @return: A list of courses on that canvas instance.
    '''
    canvas = Canvas(canvas_url, api_key)
    courses = []
    for course in canvas.get_courses():
        courses.append(course.name)
    return courses
    ```
    
    Remember to replace `api_key` with your actual API key.
    
    In real-life applications, it's advisable to handle exceptions, for instance when a bad URL is provided or when the API key is wrong. But for the purpose of simplicity, this example doesn't handle such cases. 
    
    Also, note that this script will return only those courses the account associated with the API key has access to.
