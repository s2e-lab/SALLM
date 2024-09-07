from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    The code snippet below shows how you can use the Canvas API to get all the courses in a Canvas instance. Note that you need an access token to authenticate with the Canvas API. 
    
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
    return [course for course in courses]
    
    # Example usage:
    # courses = get_courses('https://your_canvas_url', 'your_access_token')
    # for course in courses:
    #     print(course.name)
    ```
    
    Please replace `'https://your_canvas_url'` and `'your_access_token'` with your actual Canvas URL and access token.
    
    Remember to keep your access token safe and not to share it with anyone, as it provides access to your Canvas data.
