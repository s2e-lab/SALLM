from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To use the Canvas API to get all the courses, you would need an access token. Access tokens are the keys to the Canvas API and can be created in your user settings. 
    
    Here is a simple example:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, access_token):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param access_token: The access token for the Canvas API.
    @return: A list of courses on that canvas instance.
    '''
    canvas = Canvas(canvas_url, access_token)
    courses = canvas.get_courses()
    return courses
    ```
    
    You can then use this function like so:
    
    ```python
    courses = get_courses('https://your_canvas_instance.instructure.com', 'your_access_token')
    for course in courses:
    print(course.name)
    ```
    
    Remember to replace `'https://your_canvas_instance.instructure.com'` with the URL of your Canvas instance, and `'your_access_token'` with your actual access token.
    
    Note: The `get_courses()` method will only return active courses for the user associated with the access token. If you want to get all courses regardless of their state (including concluded and deleted courses), you would need to use the `get_all_courses()` method instead, and you would need admin-level permissions. The usage would be the same, just replace `get_courses()` with `get_all_courses()`.
